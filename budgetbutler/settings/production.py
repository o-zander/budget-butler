from .default import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['budget-butler.herokuapp.com']