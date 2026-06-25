from pathlib import Path
from datetime import timedelta
import os


BASE_DIR = Path(__file__).resolve().parent.parent

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

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
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
WORKER_SHARED_SECRET = os.getenv("WORKER_SHARED_SECRET", "change-me")
LOCAL_REGISTRY = os.getenv("LOCAL_REGISTRY", "localhost:5000")

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
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
