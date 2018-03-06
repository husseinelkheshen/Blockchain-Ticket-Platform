#!/usr/bin/env python
import os
import sys

if not os.environ["ADMIT01_ENV_TYPE"]:
    env = "dev"
else:
    env = "prod"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admit01.settings." + env)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
