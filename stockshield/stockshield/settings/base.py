
import os
#from stockshield.mystockapi.models import CustomUser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mystockapi.herokuapp.com','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

  #third party apps
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'rest_framework_swagger',
    'rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'corsheaders', 
    'phone_field',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    
    #local apps
    'inventory.apps.InventoryConfig',
    'users.apps.UsersConfig',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [ # new
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.TokenAuthentication',
    ],
}

REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }

'''
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'users.serializers.UserLoginSerializer',
    'PASSWORD_CHANGE_SERIALIZER': 'users.serializers.UserPasswordChangeSerializer',
    'PASSWORD_RESET_SERIALIZER': 'users.serializers.UserPasswordResetSerializer',
    'PASSWORD_RESET_CONFIRM_SERIALIZER': 'users.serializers.UserPasswordResetSerializer',
    'USER_DETAILS_SERIALIZER': 'users.serializers.UserPasswordResetSerializer',

}
'''
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'users.serializers.UserRegisterSerializer',
    
    #'TOKEN_SERIALIZER': 'path.to.custom.TokenSerializer',
    
}


MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # new
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# new
CORS_ORIGIN_WHITELIST = (
'http://localhost:3000',
'http://localhost:8000',
)


ROOT_URLCONF = 'stockshield.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
AUTH_USER_MODEL = 'users.User'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
SECRET_KEY = '*'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1

PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)



#import dj_database_url 
#prod_db  =  dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(prod_db)
