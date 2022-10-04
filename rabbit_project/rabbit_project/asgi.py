"""
ASGI config for rabbit_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

print(f"Currently translating {constants.LANGUAGES[INPUT_LANG]} to {constants.LANGUAGES[OUTPUT_LANG]}, speak to translate\n")

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rabbit_project.settings")

application = get_asgi_application()
