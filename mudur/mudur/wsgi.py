#!-*- coding:utf-8 -*-

"""
WSGI config for mudur project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
reload(sys)


path = '/home/ozge/web/mudur/'
if path not in sys.path:
   sys.path.append(path)

sys.setdefaultencoding('UTF8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mudur.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
