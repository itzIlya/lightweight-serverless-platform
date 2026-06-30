import sys
import unittest
from pathlib import Path
from unittest.mock import Mock
from urllib import error

sys.path.insert(0, str(Path(__file__).resolve().parent))

from orphan_image_cleaner import delete_registry_image, repository_and_tag


class Response:
    def __init__(self, headers=None):
        self.headers = headers or {}

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class OrphanImageCleanerTests(unittest.TestCase):
    def test_repository_and_tag_parses_attempt_image(self):
        repository, tag = repository_and_tag(
            "localhost:5000/functions/echo:v1-a1-abc-d2"
        )
        self.assertEqual(repository, "functions/echo")
        self.assertEqual(tag, "v1-a1-abc-d2")

    def test_cleanup_resolves_digest_then_deletes_manifest(self):
        opener = Mock()
        opener.side_effect = [
            Response({"Docker-Content-Digest": "sha256:abc"}),
            Response(),
        ]

        deleted = delete_registry_image(
            "localhost:5000/functions/echo:v1-a1-abc-d1",
            registry_base_url="http://registry:5000",
            urlopen=opener,
        )

        self.assertTrue(deleted)
        self.assertEqual(opener.call_args_list[0].args[0].method, "HEAD")
        self.assertIn("v1-a1-abc-d1", opener.call_args_list[0].args[0].full_url)
        self.assertEqual(opener.call_args_list[1].args[0].method, "DELETE")
        self.assertIn("sha256:abc", opener.call_args_list[1].args[0].full_url)

    def test_missing_orphan_is_idempotent_success(self):
        opener = Mock()
        opener.side_effect = error.HTTPError("url", 404, "missing", {}, None)

        deleted = delete_registry_image(
            "localhost:5000/functions/echo:v1-a1-abc-d1",
            registry_base_url="http://registry:5000",
            urlopen=opener,
        )

        self.assertFalse(deleted)
