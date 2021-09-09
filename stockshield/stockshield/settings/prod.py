'''For production settings only'''

from .base import * 

DEBUG = False
ALLOWED_HOSTS += ['*']
WSGI_APPLICATION = 'stockshield.wsgi.prod.application'

