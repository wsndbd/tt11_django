"""
WSGI config for tt11 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from os.path import join, dirname, abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))

import sys
sys.path.insert(0, PROJECT_DIR)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tt11.settings")

'''
def application(environ, start_response):
    status = "200 OK"
    if not environ['mod_wsgi.process_group']:
        output = 'EMBEDDED MODE'
    else:
        output = 'DAEMON MODE'
    response_headers = [('Content-Type', 'text/plain'),
            ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
'''

application = get_wsgi_application()

import tt11.monitor
tt11.monitor.start(interval=3.0)
