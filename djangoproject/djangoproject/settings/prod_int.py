from .prod import *

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'test',
            'USER': 'user',
            'PASSWORD': 'password',
            'HOST': 'db',
            'PORT': '5432',
    }
}

DEBUG = True
SITE_ID = 1
