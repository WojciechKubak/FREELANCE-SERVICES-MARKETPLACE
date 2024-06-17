from app.env import env_to_bool, env_to_list
from app.settings.base import *
import os


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DB", "db"),
        "USER": os.environ.get("POSTGRES_USER", "user"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
        "HOST": os.environ.get("POSTGRES_HOST", "host"),
        "PORT": os.environ.get("POSTGRES_PORT", "port"),
    }
}

ALLOWED_HOSTS = env_to_list(os.environ.get("ALLOWED_HOSTS"), "")

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = env_to_list(os.environ.get("CORS_ORIGIN_WHITELIST"), "")

SESSION_COOKIE_SECURE = env_to_bool(os.environ.get("SESSION_COOKIE_SECURE", 1))

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = env_to_bool(os.environ.get("SECURE_SSL_REDIRECT", 1))

SECURE_CONTENT_TYPE_NOSNIFF = env_to_bool(
    os.environ.get("SECURE_CONTENT_TYPE_NOSNIFF", 1)
)
