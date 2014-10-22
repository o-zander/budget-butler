from .default import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['budget-butler.herokuapp.com']