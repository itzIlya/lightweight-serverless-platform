from django.test import SimpleTestCase, override_settings

from .models import CoordinationVersion, JobType
from .services import coordination_version_for_job


class CoordinationRolloutTests(SimpleTestCase):
    @override_settings(
        V2_INVOCATION_PILOT_ENABLED=False,
        V2_INVOCATION_ROLLOUT_PERCENT=100,
        V2_INVOCATION_CANARY_FUNCTION_IDS="42",
    )
    def test_kill_switch_keeps_all_new_jobs_on_v1(self):
        selected = coordination_version_for_job(
            JobType.INVOCATION,
            "request-1",
            function_id=42,
        )

        self.assertEqual(selected, CoordinationVersion.V1)

    @override_settings(
        V2_INVOCATION_PILOT_ENABLED=True,
        V2_INVOCATION_ROLLOUT_PERCENT=0,
        V2_INVOCATION_CANARY_FUNCTION_IDS="42, invalid",
    )
    def test_zero_percent_routes_only_explicit_canary_functions(self):
        canary = coordination_version_for_job(
            JobType.INVOCATION,
            "request-1",
            function_id=42,
        )
        ordinary = coordination_version_for_job(
            JobType.INVOCATION,
            "request-2",
            function_id=43,
        )

        self.assertEqual(canary, CoordinationVersion.V2)
        self.assertEqual(ordinary, CoordinationVersion.V1)

    @override_settings(
        V2_BUILD_PILOT_ENABLED=True,
        V2_BUILD_ROLLOUT_PERCENT=25,
        V2_BUILD_CANARY_FUNCTION_IDS="",
    )
    def test_percentage_selection_is_stable_for_retries(self):
        first = coordination_version_for_job(JobType.BUILD, "build-request-1")
        repeated = coordination_version_for_job(JobType.BUILD, "build-request-1")

        self.assertEqual(first, repeated)

    @override_settings(
        V2_BUILD_PILOT_ENABLED=True,
        V2_BUILD_ROLLOUT_PERCENT=100,
        V2_BUILD_CANARY_FUNCTION_IDS="",
    )
    def test_full_rollout_selects_v2(self):
        self.assertEqual(
            coordination_version_for_job(JobType.BUILD, "build-request-1"),
            CoordinationVersion.V2,
        )

    @override_settings(
        V2_BUILD_PILOT_ENABLED=True,
        V2_INVOCATION_PILOT_ENABLED=True,
        V2_BUILD_ROLLOUT_PERCENT=100,
        V2_INVOCATION_ROLLOUT_PERCENT=100,
        V2_CUTOVER_STAGE="builds",
        V2_BUILD_CANARY_FUNCTION_IDS="",
        V2_INVOCATION_CANARY_FUNCTION_IDS="",
    )
    def test_build_stage_enables_builds_but_not_private_invocations(self):
        build = coordination_version_for_job(JobType.BUILD, "build-1")
        invocation = coordination_version_for_job(
            JobType.INVOCATION,
            "invoke-1",
            invoke_access="private",
        )

        self.assertEqual(build, CoordinationVersion.V2)
        self.assertEqual(invocation, CoordinationVersion.V1)

    @override_settings(
        V2_INVOCATION_PILOT_ENABLED=True,
        V2_INVOCATION_ROLLOUT_PERCENT=100,
        V2_INVOCATION_CANARY_FUNCTION_IDS="",
        V2_CUTOVER_STAGE="token",
    )
    def test_token_stage_includes_private_and_token_but_not_public(self):
        selected = {
            access: coordination_version_for_job(
                JobType.INVOCATION,
                f"invoke-{access}",
                invoke_access=access,
            )
            for access in ("private", "token", "public")
        }

        self.assertEqual(selected["private"], CoordinationVersion.V2)
        self.assertEqual(selected["token"], CoordinationVersion.V2)
        self.assertEqual(selected["public"], CoordinationVersion.V1)

    @override_settings(
        V2_INVOCATION_PILOT_ENABLED=True,
        V2_INVOCATION_ROLLOUT_PERCENT=0,
        V2_INVOCATION_CANARY_FUNCTION_IDS="42",
        V2_CUTOVER_STAGE="internal",
    )
    def test_internal_stage_routes_only_canary_function(self):
        canary = coordination_version_for_job(
            JobType.INVOCATION,
            "invoke-canary",
            function_id=42,
            invoke_access="public",
        )
        ordinary = coordination_version_for_job(
            JobType.INVOCATION,
            "invoke-ordinary",
            function_id=43,
            invoke_access="private",
        )

        self.assertEqual(canary, CoordinationVersion.V2)
        self.assertEqual(ordinary, CoordinationVersion.V1)

    @override_settings(
        V2_INVOCATION_PILOT_ENABLED=True,
        V2_INVOCATION_ROLLOUT_PERCENT=0,
        V2_INVOCATION_CANARY_FUNCTION_IDS="",
        V2_CUTOVER_STAGE="all",
        V1_JOB_CREATION_ENABLED=False,
    )
    def test_v1_creation_switch_rejects_incomplete_cutover(self):
        with self.assertRaisesRegex(RuntimeError, "V1 job creation is disabled"):
            coordination_version_for_job(
                JobType.INVOCATION,
                "invoke-1",
                invoke_access="public",
            )
