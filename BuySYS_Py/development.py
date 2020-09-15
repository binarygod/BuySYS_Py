import os
from .common import *

# Postgress pgpass.conf in %AppData%\Roaming\postgresql
# Install PostGres Tools


SECRET_KEY = 'enpiw%+i5&y29g4@^jw7bfq4#r!&*mg%ul)-12x^-^pd)c9$-&'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.postgresql_psycopg2',
        'NAME'    : 'buysys',
        'USER'    : 'postgres',
        'PASSWORD': 'ILoveWhisky',
        'HOST'    : '10.0.1.13',
        'PORT'    : ''
    }
}

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'node_modules'
]
