"""Settings for CI environment."""
from sampleproject.settings.base import *  # noqa


ENVIRONMENT = 'ci'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9(*ru&g0i*@3&it)(&&c#5d8--1ne9cg%a!n5hj9+x9ts0wr84'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
