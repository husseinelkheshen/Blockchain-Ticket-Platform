"""
WSGI config for admit01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if not os.environ["ADMIT01_ENV_TYPE"]:
    env = "dev"
else:
    env = "prod"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admit01.settings." + env)

application = get_wsgi_application()
