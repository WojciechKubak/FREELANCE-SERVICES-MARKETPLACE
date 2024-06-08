from app.settings.base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "db_1",
        "USER": "user",
        "PASSWORD": "user1234",
        "HOST": "db_test",
        "PORT": "5433",
    }
}
