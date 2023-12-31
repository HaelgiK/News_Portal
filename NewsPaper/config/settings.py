"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

import logging
from config.logging_formaters import CustomJsonFormatter

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3hj-&9n1u1piaa%54orox@#@!31cumhiq+&ay-f+#&$qz*g!=t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'modeltranslation', # это приложение
    # обязательно надо вписать перед админом
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # add apps
    'news',
    'accounts',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'news.middlewares.TimezoneMiddleware',
]


ROOT_URLCONF = 'config.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Russian'),
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # Указываем, куда будем сохранять кэшируемые файлы
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Belgrade'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

ADMINS = (
    (os.getenv('ADMIN_USER'), os.getenv('EMAIL_ADMIN')),
)
EMAIL_HOST = 'smtp.mail.ru' # адрес сервера Яндекс-почты для всех один и тот же
#EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 2525 #465порт smtp сервера тоже одинаковый
# имя пользователя, всё то EMAIL_HOST_USER = 'oleg18.09'что в почте до собаки
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# Яндекс использует ssl, включать его здесь обязательно
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_ADMIN = os.getenv('EMAIL_ADMIN')
SERVER_EMAIL = os.getenv('SERVER_EMAIL')
ADMIN_USER = os.getenv('ADMIN_USER')

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Конкретизация URL-адреса, на котором находится страница аутентификации
LOGIN_URL = '/accounts/login/'
# Страница, на которую перенаправляется пользователь
# после успешного входа на сайт,
# в данном случае корневая страница сайта
LOGIN_REDIRECT_URL = '/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# Верификация почты через подтверждение аккаунта
ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_FORMS = {'signup': 'sign.forms.CommonSignupForm'}

SITE_URL = 'http://127.0.0.1:8000'

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

# Указываем на URL брокера сообщений (Redis).
# По умолчанию он находится на порту 6379
CELERY_BROKER_URL = 'redis://localhost:6379'
# указываем на хранилище результатов выполнения задач
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# допустимый формат данных
CELERY_ACCEPT_CONTENT = ['application/json']
# метод сериализации задач
CELERY_TASK_SERIALIZER = 'json'
# метод сериализации результатов
CELERY_RESULT_SERIALIZER = 'json'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters' : {
        'debug_form': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'warning_form': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'error_form': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'general_form': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'mail_form': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'json_formatter': {
            '()': CustomJsonFormatter,
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'debug_form'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning_form'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error_form'
        },
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'logs/general.log',
            'formatter': 'general_form'
        },
        'file_json': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'logs/json.log',
            'formatter': 'json_formatter'
        },
        'file_errors': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
            'formatter': 'error_form'
        },
        'file_security': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'logs/security.log',
            'formatter': 'general_form'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mail_form'
        }
    },
    'loggers': {
        'django': {
            'handlers': [
                'console', 'console_warning',
                'console_error', 'file_general', 'file_json'
            ],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_errors', 'mail_admins'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['file_errors', 'mail_admins'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file_errors'],
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['file_errors'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': [
#         'django_filters.rest_framework.DjangoFilterBackend'
#     ],
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 10,
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#     ],
#     'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
# }
#
# SPECTACULAR_SETTINGS = {
#     "TITLE": "MP List API", # название проекта
#     "DESCRIPTION": 'API documentation for application PASS_APP',
#     "VERSION": "0.0.1", # версия проекта
#     "SERVE_INCLUDE_SCHEMA": False, # исключить эндпоинт /schema
#     "SWAGGER_UI_SETTINGS": {
#         "filter": True, # включить поиск по тегам
#     },
#     "COMPONENT_SPLIT_REQUEST": True
# }
