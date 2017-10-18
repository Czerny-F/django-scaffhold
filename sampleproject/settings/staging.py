"""Settings for staging server."""
from sampleproject.settings.base import *  # noqa


ENVIRONMENT = 'staging'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9(*ru&g0i*@3&it)(&&c#5d8--1ne9cg%a!n5hj9+x9ts0wr84'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['localhost']


# Application definition

ROOT_URLCONF = 'sampleproject.urls'

WSGI_APPLICATION = 'sampleproject.wsgi.application'


# django-nose

INSTALLED_APPS += [
    'django_nose',
]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = ['--rednose']


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(
                os.path.dirname(os.path.dirname(BASE_DIR)), 'my.cnf'),
            'sql_mode': 'TRADITIONAL',
        },
    }
}

STATIC_ROOT = '/var/www/html/static/'
