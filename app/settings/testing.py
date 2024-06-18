from app.settings.base import *


EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

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


PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
