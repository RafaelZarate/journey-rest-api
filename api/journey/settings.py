
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

ENV_PROD = False
ENV_LOCAL = False

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost']

if os.environ.get('ENVIRONMENT', '') == 'PRODUCTION':
    CORS_ORIGIN_ALLOW_ALL = ['http://127.0.0.1:3000']
    ENV_PROD = True
    ENVIRONMENT = 'PRODUCTION'
    API_HOST = 'tbd'
    PWA_HOST = 'tbd'
    DEV_MODE = False
    DEBUG = False
else:
    CORS_ORIGIN_ALLOW_ALL = True
    ENV_LOCAL = True
    ENVIRONMENT = 'LOCAL'
    API_HOST = 'http://localhost:8000'
    PWA_HOST = 'http://localhost:3000'
    DEV_MODE = True
    DEBUG = True
    SHOW_DEBUG_TOOLBAR = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders',
    # 'django_filters',
    'core',
    'api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'journey.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'journey.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if ENV_PROD:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': os.environ['REDIS_ENDPOINT'],
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
            }
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'journey',
            'USER': 'journeyadmin',
            'PASSWORD': 'AS159erty',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://0.0.0.0:6379/1',
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
            }
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

JWT_VERIFY = True
JWT_VERIFY_EXPIRATION = False
JWT_AUTH_HEADER_PREFIX = 'Auth-Journey'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

SWAGGER_SETTINGS = {
    'APIS_SORTER': 'alpha',
    'DOC_EXPANSION': None,
    'JSON_EDITOR': True,
    'OPERATIONS_SORTER': 'method',
    'SHOW_REQUEST_HEADERS': True,

}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        # 'rest_framework.parsers.FormParser',
        'rest_framework.parsers.JSONParser',
    )
}
