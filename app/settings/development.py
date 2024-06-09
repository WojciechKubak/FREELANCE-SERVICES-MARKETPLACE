from app.settings.base import *


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

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
