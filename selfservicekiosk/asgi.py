"""
ASGI config for selfservicekiosk project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from decouple import config as env
from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"selfservicekiosk.settings.{env('ENVIROMENT', cast=str)}"
)

application = get_asgi_application()
