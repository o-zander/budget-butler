from .default import *

SECRET_KEY = '!4an791w31rha_#m26(5io-9woqk)@x&*&m9mrmf3vsgxw=oew'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = '*'

PIPELINE_ENABLED = False