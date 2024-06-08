"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
from app.settings.base import DEBUG
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "app.settings.development" if DEBUG else "app.settings.production",
)

application = get_wsgi_application()
