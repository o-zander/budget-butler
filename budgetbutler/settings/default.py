# coding=utf-8
from __future__ import unicode_literals

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
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

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

PIPELINE_ENABLED = True
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_CSS = {
    'styles': {
        'source_filenames': (
            'css/framework7.min.css',
            'css/framework7.themes.min.css',
            'less/custom-style.less',
        ),
        'output_filename': 'min/css/style.min.css',
    },
}
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
            'js/libs/jquery.min.js',
            'js/libs/framework7.min.js',
            'js/budget-butler.js',
        ),
        'output_filename': 'min/js/script.min.js',
    }
}
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)
PIPELINE_DISABLE_WRAPPER = True

CURRENCY = '€'
