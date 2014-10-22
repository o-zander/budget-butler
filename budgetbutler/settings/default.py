import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'budgetbutler.urls'

WSGI_APPLICATION = 'budgetbutler.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'de-DE'

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'conf', 'locale'),
)

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'budgetbutler',

    'pipeline',
)

PIPELINE_CSS = {
    'style': {
        'source_filenames': (
            'css/bootstrap.min.css',
            'less/custom-style.less',
        ),
        'output_filename': 'min/css/style.min.css',
    },
}
PIPELINE_JS = {
    'script': {
        'source_filenames': (
            'js/libs/jquery-2.1.1.min.js',
            'js/libs/bootstrap.min.js',
            'js/libs/react-0.11.2.min.js',
            'jsx/apps.jsx'
        ),
        'output_filename': 'min/js/script.min.js',
    }
}
PIPELINE_COMPILERS = (
    'react.utils.pipeline.JSXCompiler',
    'pipeline.compilers.less.LessCompiler',
)
PIPELINE_DISABLE_WRAPPER = True
