from app.settings.base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db_1",
        "USER": "user",
        "PASSWORD": "user1234",
        "HOST": "db_dev",
        "PORT": "5432",
    }
}
