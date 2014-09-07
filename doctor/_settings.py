import os
import sys
from os.path import join, dirname, realpath

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '#ae&b_k==wsfc$x9j(gjt3#a8scvq8khvo9subu-p-2cbx8*z='

PROJECT_ROOT = realpath(join(dirname(__file__), '../..'))
ROOT_PATH = realpath(join(dirname(__file__), '..'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

PANEL_PAGE_SIZE = 10

CRISPY_TEMPLATE_PACK = 'foundation-5'

# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.doc',
    'crispy_forms',
    'crispy_forms_foundation',
    'apps.common',
    'social.apps.django_app.default'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'doctor.urls'

WSGI_APPLICATION = 'doctor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'doctor',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ''

MEDIA_URL = '/media/'
MEDIA_ROOT = join(ROOT_PATH, 'media')

STATICFILES_DIRS = (
    join(ROOT_PATH, 'static'),
    join(ROOT_PATH, 'media')
)

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test_spiral',
            }
    }
    SOUTH_TESTS_MIGRATE = False
    FIREBUG = True

#Social Auth

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.linkedin.LinkedinOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'apps.core.accounts.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.user.get_username',
    # 'social.pipeline.user.create_user',
    'apps.core.social.create_user'
)

#Facebook

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '631119476924488'
SOCIAL_AUTH_FACEBOOK_SECRET = '126f064c4c3e0cb6d8ebbd42e0fe7042'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
