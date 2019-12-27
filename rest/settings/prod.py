""" Production Settings """

import os
import dj_database_url
from .dev import *

############
# DATABASE #
############

# DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
############
# SECURITY #
############

DEBUG = bool(os.getenv('DJANGO_DEBUG', ''))

if not DEBUG:
    '''remove debug_toolbar'''
    try:
        INSTALLED_APPS.remove('debug_toolbar')
        MIDDLEWARE.remove('debug_toolbar.middleware.DebugToolbarMiddleware')
    except ValueError:
        pass

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
# ALLOWED_HOSTS = ['vue-django-rest-framework.herokuapp.com']
ALLOWED_HOSTS = ['*']
