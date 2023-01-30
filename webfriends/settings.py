import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# Generate a new unique key with e.g. https://djecrety.ir/ before running
# in production.
SECRET_KEY = config("SECRET_KEY")

# Email configuration
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ALLOWED_HOSTS = []
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
SERVER_EMAIL = config("SERVER_EMAIL")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = config("EMAIL_PORT")

#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_HOST_USER = os.environ['SENDGRID_USER']
#EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'registration',
    'crispy_forms',
    'fof.apps.FoFConfig',
    'image.apps.ImageProcessingConfig',
    'resulttable.apps.ResultConfig',
    'webfriends.apps.WebFriendsConfig',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'webfriends.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webfriends.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'fofdb.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(
    os.path.dirname(BASE_DIR), "static")
#    os.path.dirname(BASE_DIR), "static_in_env", "static_root")

STATICFILES_DIRS = [
    os.path.join(STATIC_ROOT, "root"),
    os.path.join(BASE_DIR, "static", "ui"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/tmp/media/'

# crispy
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django registration redux
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
REGISTRATION_EMAIL_HTML = False

SITE_ID = 2

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'

# Celery CONFIGURATION
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Sao_Paulo'
CELERY_ENABLE_UTC = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

# CELERY_RESULT_BACKEND = 'rpc://'
# CELERY_RESULT_PERSISTENT = True
