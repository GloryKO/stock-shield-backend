'''For production settings only'''
import django_heroku
from .base import * 

DEBUG = False
ALLOWED_HOSTS += ['*']
WSGI_APPLICATION = 'stockshield.wsgi.prod.application'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
django_heroku.settings(locals())