'''For production settings only'''
import django_heroku
from .base import * 

DEBUG = True
ALLOWED_HOSTS += ['*']
WSGI_APPLICATION = 'stockshield.wsgi.prod.application'
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
django_heroku.settings(locals())