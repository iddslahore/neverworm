"""
Django settings for neverworm project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')!f&u@sqef6nn8=!b%x+qz5niob)p@560)^gosydbjzhvn($*q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'twitter_bootstrap',
#    'pipeline',
    'users',
    'orders',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'neverworm.urls'

# Settings for asset pipeline

# PIPELINE = {
#     'PIPELINE_ENABLED': True,
#     'JS_COMPRESSOR' : '',
#     'CSS_COMPRESSOR' : '',
#     'COMPILERS': ['pipeline.compilers.less.LessCompiler',],
#     'STYLESHEETS': {
#         'bootstrap': {
#             'source_filenames': (
#                 'twitter_bootstrap/less/bootstrap.less',
#             ),
#             'output_filename': 'css/bootstrap.css',
#             'extra_context': {
#                 'media': 'screen,projection',
#             },
#         },
#     },
#      'JAVASCRIPT' : {
#          'bootstrap': {
#              'source_filenames': (
#                  'twitter_bootstrap/js/transition.js',
#                  'twitter_bootstrap/js/modal.js',
#                  'twitter_bootstrap/js/dropdown.js',
#                  'twitter_bootstrap/js/scrollspy.js',
#                  'twitter_bootstrap/js/tab.js',
#                  'twitter_bootstrap/js/tooltip.js',
#                  'twitter_bootstrap/js/popover.js',
#                  'twitter_bootstrap/js/alert.js',
#                  'twitter_bootstrap/js/button.js',
#                  'twitter_bootstrap/js/collapse.js',
#                  'twitter_bootstrap/js/carousel.js',
#                  'twitter_bootstrap/js/affix.js',
#              ),
#             'output_filename': 'js/bootstrap.js',
#          },
#      },
# }

# Settings for django-bootstrap3
# BOOTSTRAP3 = {
#     'set_required': False,
#     'error_css_class': 'bootstrap3-error',
#     'required_css_class': 'bootstrap3-required',
#     'javascript_in_head': True,
# }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'neverworm/templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request':{
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'orders':{
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'users':{
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'tracking':{
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    },
}

LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'neverworm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {}
if os.environ.get('DATABASE_URL'):
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()
else:
    DATABASES['default'] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }

# Heroku
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'neverworm/static'),
)

#STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

#App stuff
DEADLINE_DELTA_DAYS = 6
