from app.env import env_to_bool, env_to_int
import os


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_USE_TLS = env_to_bool(os.environ.get("EMAIL_USE_TLS"))
EMAIL_USE_SSL = env_to_bool(os.environ.get("EMAIL_USE_SSL"))
EMAIL_PORT = env_to_int(os.environ.get("EMAIL_PORT"))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
