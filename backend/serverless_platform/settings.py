from pathlib import Path
from datetime import timedelta
import os
import sys


BASE_DIR = Path(__file__).resolve().parent.parent


def env_bool(name: str, default: str = "false") -> bool:
    return os.getenv(name, default).lower() in {"1", "true", "yes"}


def env_list(name: str, default: str = "") -> list[str]:
    return [
        item.strip()
        for item in os.getenv(name, default).split(",")
        if item.strip()
    ]


def normalize_endpoint_url(value: str) -> str:
    value = str(value or "").strip()
    if value and "://" not in value:
        return f"https://{value}"
    return value

SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-secret-key")
DEBUG = os.getenv("DEBUG", "1") == "1"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("ALLOWED_HOSTS", "*").split(",")
    if host.strip()
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "apps.accounts.apps.AccountsConfig",
    "apps.health.apps.HealthConfig",
    "apps.functions.apps.FunctionsConfig",
    "apps.invocations.apps.InvocationsConfig",
    "apps.jobs.apps.JobsConfig",
    "apps.workers.apps.WorkersConfig",
]

TESTING = "test" in sys.argv
OBJECT_STORAGE_ENABLED = env_bool("OBJECT_STORAGE_ENABLED") and not TESTING
OBJECT_STORAGE_ENDPOINT_URL = normalize_endpoint_url(
    os.getenv("OBJECT_STORAGE_ENDPOINT_URL", "")
)
OBJECT_STORAGE_ACCESS_KEY_ID = os.getenv("OBJECT_STORAGE_ACCESS_KEY_ID", "")
OBJECT_STORAGE_SECRET_ACCESS_KEY = os.getenv("OBJECT_STORAGE_SECRET_ACCESS_KEY", "")
OBJECT_STORAGE_BUCKET_NAME = os.getenv("OBJECT_STORAGE_BUCKET_NAME", "")
OBJECT_STORAGE_REGION_NAME = os.getenv("OBJECT_STORAGE_REGION_NAME", "us-east-1")
OBJECT_STORAGE_FORCE_PATH_STYLE = env_bool("OBJECT_STORAGE_FORCE_PATH_STYLE", "true")
OBJECT_STORAGE_MEDIA_LOCATION = os.getenv("OBJECT_STORAGE_MEDIA_LOCATION", "media")

if OBJECT_STORAGE_ENABLED:
    INSTALLED_APPS.append("storages")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "serverless_platform.cors.FrontendCorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOWED_ORIGINS = env_list(
    "CORS_ALLOWED_ORIGINS",
    "http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000,http://127.0.0.1:3000",
)
CORS_ALLOW_ALL_ORIGINS = env_bool("CORS_ALLOW_ALL_ORIGINS")
CORS_ALLOW_CREDENTIALS = env_bool("CORS_ALLOW_CREDENTIALS")
CORS_ALLOWED_METHODS = env_list(
    "CORS_ALLOWED_METHODS",
    "GET,POST,PUT,PATCH,DELETE,OPTIONS",
)
CORS_ALLOWED_HEADERS = env_list(
    "CORS_ALLOWED_HEADERS",
    "authorization,content-type,x-function-token,x-invocation-read-token,x-requested-with",
)
CORS_EXPOSE_HEADERS = env_list(
    "CORS_EXPOSE_HEADERS",
    "content-disposition,content-length,retry-after",
)
CORS_PREFLIGHT_MAX_AGE = int(os.getenv("CORS_PREFLIGHT_MAX_AGE", "86400"))

ROOT_URLCONF = "serverless_platform.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "serverless_platform.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "serverless"),
        "USER": os.getenv("POSTGRES_USER", "serverless"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "serverless"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

if OBJECT_STORAGE_ENABLED:
    missing_object_storage_settings = [
        name
        for name, value in {
            "OBJECT_STORAGE_ENDPOINT_URL": OBJECT_STORAGE_ENDPOINT_URL,
            "OBJECT_STORAGE_ACCESS_KEY_ID": OBJECT_STORAGE_ACCESS_KEY_ID,
            "OBJECT_STORAGE_SECRET_ACCESS_KEY": OBJECT_STORAGE_SECRET_ACCESS_KEY,
            "OBJECT_STORAGE_BUCKET_NAME": OBJECT_STORAGE_BUCKET_NAME,
        }.items()
        if not value
    ]
    if missing_object_storage_settings:
        raise RuntimeError(
            "Object storage is enabled but missing settings: "
            + ", ".join(missing_object_storage_settings)
        )

    object_storage_options = {
        "bucket_name": OBJECT_STORAGE_BUCKET_NAME,
        "endpoint_url": OBJECT_STORAGE_ENDPOINT_URL,
        "access_key": OBJECT_STORAGE_ACCESS_KEY_ID,
        "secret_key": OBJECT_STORAGE_SECRET_ACCESS_KEY,
        "region_name": OBJECT_STORAGE_REGION_NAME,
        "default_acl": None,
        "querystring_auth": True,
        "file_overwrite": False,
        "location": OBJECT_STORAGE_MEDIA_LOCATION,
        "signature_version": "s3v4",
    }
    if OBJECT_STORAGE_FORCE_PATH_STYLE:
        object_storage_options["addressing_style"] = "path"

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": object_storage_options,
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
ORCHESTRATOR_BASE_URL = os.getenv(
    "ORCHESTRATOR_BASE_URL",
    "http://orchestrator:8010",
)
ORCHESTRATOR_EVENT_STREAM = os.getenv(
    "ORCHESTRATOR_EVENT_STREAM",
    "orchestrator:events",
)
V2_BUILD_PILOT_ENABLED = os.getenv("V2_BUILD_PILOT_ENABLED", "false").lower() in {
    "1",
    "true",
    "yes",
}
V2_INVOCATION_PILOT_ENABLED = os.getenv(
    "V2_INVOCATION_PILOT_ENABLED",
    "false",
).lower() in {"1", "true", "yes"}
V2_BUILD_ROLLOUT_PERCENT = max(
    0,
    min(100, int(os.getenv("V2_BUILD_ROLLOUT_PERCENT", "100"))),
)
V2_INVOCATION_ROLLOUT_PERCENT = max(
    0,
    min(100, int(os.getenv("V2_INVOCATION_ROLLOUT_PERCENT", "100"))),
)
V2_BUILD_CANARY_FUNCTION_IDS = os.getenv("V2_BUILD_CANARY_FUNCTION_IDS", "")
V2_INVOCATION_CANARY_FUNCTION_IDS = os.getenv(
    "V2_INVOCATION_CANARY_FUNCTION_IDS",
    "",
)
V2_CUTOVER_STAGE = os.getenv("V2_CUTOVER_STAGE", "all").strip().lower()
V1_JOB_CREATION_ENABLED = os.getenv(
    "V1_JOB_CREATION_ENABLED",
    "true",
).lower() in {"1", "true", "yes"}
V1_COORDINATION_ENDPOINTS_ENABLED = os.getenv(
    "V1_COORDINATION_ENDPOINTS_ENABLED",
    "true",
).lower() in {"1", "true", "yes"}
SYNC_INVOCATION_TIMEOUT_SECONDS = float(
    os.getenv("SYNC_INVOCATION_TIMEOUT_SECONDS", "15")
)
SYNC_INVOCATION_POLL_INTERVAL_SECONDS = float(
    os.getenv("SYNC_INVOCATION_POLL_INTERVAL_SECONDS", "0.1")
)
SYNC_INVOCATION_MAX_RESULT_BYTES = int(
    os.getenv("SYNC_INVOCATION_MAX_RESULT_BYTES", "262144")
)
SYNC_INVOCATION_MAX_STDOUT_BYTES = int(
    os.getenv("SYNC_INVOCATION_MAX_STDOUT_BYTES", "65536")
)
SYNC_INVOCATION_MAX_STDERR_BYTES = int(
    os.getenv("SYNC_INVOCATION_MAX_STDERR_BYTES", "65536")
)
JOB_QUEUE_NAME = os.getenv(
    "JOB_QUEUE_NAME",
    os.getenv(
        "INVOCATION_QUEUE_NAME",
        os.getenv("QUEUE_NAME", "function-jobs"),
    ),
)
INVOCATION_QUEUE_NAME = os.getenv(
    "INVOCATION_QUEUE_NAME",
    JOB_QUEUE_NAME,
)
SCHEDULER_QUEUE_NAME = os.getenv("SCHEDULER_QUEUE_NAME", "scheduler-pending-jobs")
SCHEDULER_INVOCATION_QUEUE_NAME = os.getenv(
    "SCHEDULER_INVOCATION_QUEUE_NAME",
    "scheduler-pending-invocations",
)
SCHEDULER_BUILD_QUEUE_NAME = os.getenv(
    "SCHEDULER_BUILD_QUEUE_NAME",
    "scheduler-pending-builds",
)
WORKER_QUEUE_PREFIX = os.getenv("WORKER_QUEUE_PREFIX", "worker")
WORKER_STALE_AFTER_SECONDS = int(os.getenv("WORKER_STALE_AFTER_SECONDS", "30"))
JOB_RECOVERY_MAX_ATTEMPTS_BUILD = int(
    os.getenv("JOB_RECOVERY_MAX_ATTEMPTS_BUILD", "3")
)
JOB_RECOVERY_MAX_ATTEMPTS_INVOCATION = int(
    os.getenv("JOB_RECOVERY_MAX_ATTEMPTS_INVOCATION", "3")
)
JOB_RECOVERY_BACKOFF_SECONDS_BUILD = os.getenv(
    "JOB_RECOVERY_BACKOFF_SECONDS_BUILD",
    "10,30,120",
)
JOB_RECOVERY_BACKOFF_SECONDS_INVOCATION = os.getenv(
    "JOB_RECOVERY_BACKOFF_SECONDS_INVOCATION",
    "0,2,8",
)
INVOCATION_RETENTION_DAYS = int(os.getenv("INVOCATION_RETENTION_DAYS", "7"))
DEAD_LETTER_RETENTION_DAYS = int(os.getenv("DEAD_LETTER_RETENTION_DAYS", "60"))
WORKER_SHARED_SECRET = os.getenv("WORKER_SHARED_SECRET", "change-me")
LOCAL_REGISTRY = os.getenv("LOCAL_REGISTRY", "localhost:5000")
REGISTRY_IMAGE_REF_HOST = os.getenv("REGISTRY_IMAGE_REF_HOST", LOCAL_REGISTRY)
REGISTRY_INTERNAL_BASE_URL = os.getenv(
    "REGISTRY_INTERNAL_BASE_URL",
    "http://registry:5000",
)
MAX_ACTIVE_INVOKE_TOKENS_PER_FUNCTION = int(
    os.getenv("MAX_ACTIVE_INVOKE_TOKENS_PER_FUNCTION", "20")
)
USERSERVICE_JWT_ALGORITHM = os.getenv("USERSERVICE_JWT_ALGORITHM", "RS256")
USERSERVICE_JWT_ISSUER = os.getenv(
    "USERSERVICE_JWT_ISSUER",
    "serverless-userservice",
)
USERSERVICE_JWT_AUDIENCE = os.getenv(
    "USERSERVICE_JWT_AUDIENCE",
    "serverless-platform",
)
USERSERVICE_JWKS_URL = os.getenv("USERSERVICE_JWKS_URL", "")
USERSERVICE_JWKS_CACHE_SECONDS = int(
    os.getenv("USERSERVICE_JWKS_CACHE_SECONDS", "300")
)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "apps.accounts.external_auth.ExternalUserServiceJWTAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}
