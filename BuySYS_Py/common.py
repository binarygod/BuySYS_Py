import os
import sys
from pathlib import Path
from .branding import *

# http://localhost:8000/oidc/eveonline/complete
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(os.path.normpath(os.path.join(BASE_DIR, 'apps')))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_core',
    'social_django',
    'apps.bg_eveonline_auth',
    'apps.bg_eveonline_sde',
    'apps.bg_eveonline_sde.invTypes',
    'apps.bg_eveonline_sde.invMarketGroups',
    'apps.bg_eveonline_sde.invGroups',
    'apps.bg_eveonline_sde.dgmTypeAttributes',
    'apps.bg_eveonline_sde.invTypeMaterials',
    'apps.bg_buysys'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BuySYS_Py.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'apps.bg_eveonline_auth.backends.EVEOnlineOAuth2v2',
    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'BuySYS_Py.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
# SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_EVEONLINEV2_KEY = '4ad43d35704a4a55bb2c95c644d68e8e'
SOCIAL_AUTH_EVEONLINEV2_SECRET = 'entLVHFHcU1b4raTcGlEroaUf7Gq49nkpbn3AUXu'
SOCIAL_AUTH_CLEAN_USERNAMES = False
