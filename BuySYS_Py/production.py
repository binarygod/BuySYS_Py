import os
from .common import *


SECRET_KEY = 'enpiw%+i5&y29g4@^jw7bfq4#r!&*mg%ul)-12x^-^pd)c9$-&'

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
