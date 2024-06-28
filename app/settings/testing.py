from app.settings.base import *
import os


EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db_1",
        "USER": "user",
        "PASSWORD": "user1234",
        "HOST": "db_test",
        "PORT": "5432",
        "TEST": {
            "NAME": "db_1",
        },
    }
}
# based on https://www.hacksoft.io/blog/github-actions-in-action-setting-up-django-and-postgres
if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
