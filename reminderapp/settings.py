# Django settings for the project.

try:
    from settings_local import *
except ImportError: 
    pass

DEBUG = True   

# heroku db settings
import dj_database_url
DATABASES = {
    'default':  dj_database_url.config()
}

