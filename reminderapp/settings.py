# Django settings for the project.

try:
    from base_settings import *
except ImportError: 
    pass

DEBUG = False

# heroku db settings
import dj_database_url
DATABASES = {
    'default':  dj_database_url.config()
}

