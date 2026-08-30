from datetime import timedelta
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


def env_bool(name: str, default: str = "false") -> bool:
    return os.getenv(name, default).lower() in {"1", "true", "yes"}


def env_list(name: str, default: str = "") -> list[str]:
    return [
        item.strip()
        for item in os.getenv(name, default).split(",")
        if item.strip()
    ]


SECRET_KEY = os.getenv("USERSERVICE_SECRET_KEY", "dev-userservice-secret-key")
DEBUG = os.getenv("DEBUG", "1") == "1"
ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("USERSERVICE_ALLOWED_HOSTS", "*").split(",")
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
    "apps.accounts.apps.AccountsConfig",
    "apps.health.apps.HealthConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "userservice.cors.FrontendCorsMiddleware",
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
    "authorization,content-type,x-requested-with",
)
CORS_EXPOSE_HEADERS = env_list(
    "CORS_EXPOSE_HEADERS",
    "content-disposition,content-length,retry-after",
)
CORS_PREFLIGHT_MAX_AGE = int(os.getenv("CORS_PREFLIGHT_MAX_AGE", "86400"))

ROOT_URLCONF = "userservice.urls"

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

WSGI_APPLICATION = "userservice.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("USERSERVICE_POSTGRES_DB", "userservice"),
        "USER": os.getenv("USERSERVICE_POSTGRES_USER", "userservice"),
        "PASSWORD": os.getenv("USERSERVICE_POSTGRES_PASSWORD", "userservice"),
        "HOST": os.getenv("USERSERVICE_POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("USERSERVICE_POSTGRES_PORT", "5432"),
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
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

JWT_ISSUER = os.getenv("USERSERVICE_JWT_ISSUER", "serverless-userservice")
JWT_AUDIENCE = os.getenv("USERSERVICE_JWT_AUDIENCE", "serverless-platform")
JWT_ALGORITHM = "RS256"
JWT_ACCESS_TOKEN_LIFETIME = timedelta(
    minutes=int(os.getenv("USERSERVICE_ACCESS_TOKEN_MINUTES", "15"))
)
JWT_REFRESH_TOKEN_LIFETIME = timedelta(
    days=int(os.getenv("USERSERVICE_REFRESH_TOKEN_DAYS", "7"))
)
JWT_KEY_PATH = Path(os.getenv("USERSERVICE_JWT_KEY_PATH", BASE_DIR / "keys" / "jwt_private.pem"))

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "apps.accounts.authentication.UserServiceJWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}
