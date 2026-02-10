#!/usr/bin/env python3
# WSGI - واجهة بوابة البوابة - Web Server Gateway Interface

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()
