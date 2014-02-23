# Django settings for the project.

try:
    from settings_local import *
except ImportError:
    pass

DEBUG = False

# heroku db settings
import dj_database_url
DATABASES = {
	'default':  dj_database_url.config()
}


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS += ()
