# Django settings for the project for prod only. 

try:
    from base_settings import *
except ImportError: 
    pass

DEBUG = True   
TEMPLATE_DEBUG = DEBUG

# heroku db settings
import dj_database_url
DATABASES = {
    'default':  dj_database_url.config()
}

import os.path
PROJECT_DIR = os.path.dirname(__file__) # this is not Django setting.
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "/app/templates"), #I hacked this together, unclear if correct
    # here you can add another templates directory if you wish.
)

# Static asset configuration
import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

