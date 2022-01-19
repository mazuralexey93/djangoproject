from .prod import *

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'test',
            'USER': 'user',
            'PASSWORD': 'password',
            'HOST': '127.0.0.1',
            'PORT': '54322',
    }
}
DEBUG = True
SITE_ID = 1
