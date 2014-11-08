import dj_database_url

from .default import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DATABASES = {
    'default': dj_database_url.config()
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['budget-butler.herokuapp.com']