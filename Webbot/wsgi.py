"""
WSGI config for Webbot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/ps_wdb2015/Webbot')

os.environ["DJANGO_SETTINGS_MODULE"] = "Webbot.settings"

application = get_wsgi_application()

