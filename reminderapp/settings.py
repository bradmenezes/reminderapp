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

