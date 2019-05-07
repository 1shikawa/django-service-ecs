"""
Django settings for django_service project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ml2-isq$o5n*c7!a2g*#nd$hq=0w)@tdbzq#1v502sy2!v_+-q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Sample.apps.SampleConfig',
    'django.contrib.sites',  # Django-allauth
    'allauth',  # Django-allauth
    'allauth.account',  # Django-allauth
    'allauth.socialaccount',  # Django-allauth
    'accounts',
    'mycalendar',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'django_service.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
        'USER': 'mysiteuser',
        'PASSWORD': 'mysitepass',
        'HOST': 'django-service.ceqjvsgw7652.ap-northeast-1.rds.amazonaws.com',
        # 'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


##################
# Authentication #
##################
# 定義済み拡張ユーザーモデルを利用
AUTH_USER_MODEL = 'accounts.CustomUser'

# 認証方式を「メールアドレスとパスワード」に変更
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ユーザー名は使用しない
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ログアウト確認を非表示
ACCOUNT_LOGOUT_ON_GET = True

# ユーザー登録確認メールを送信する
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# メールアドレスを必須項目にする
ACCOUNT_EMAIL_REQUIRED = True

SITE_ID = 1

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
# LOGIN_REDIRECT_URL = '/month_with_schedule/'  # 追記箇所
LOGIN_URL = '/accounts/login/'  # 追記箇所
LOGOUT_REDIRECT_URL = '/'  # 追記箇所
# ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'


##########################
# Email SendGrid setting #
##########################
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
EMAIL_HOST = 'ishi-work.ml'
DEFAULT_FROM_EMAIL ='notify@ishi-work.ml'
SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
SENDGRID_SANDBOX_MODE_IN_DEBUG = False