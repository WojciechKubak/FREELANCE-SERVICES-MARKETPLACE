from app.settings.base import *
import os


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
