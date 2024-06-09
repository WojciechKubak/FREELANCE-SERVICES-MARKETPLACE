from app.settings.base import *


EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "db_1",
        "USER": "user",
        "PASSWORD": "user1234",
        "HOST": "db_test",
        "PORT": "5433",
        "TEST": {
            "NAME": "db_test",
        },
    }
}
