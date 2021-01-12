"""
Django settings for event_management project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#production
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#local
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@t^0jg7bruri)@_x1e6+2_*hn^!@8wnjab+bjk+qyqr)mnji4s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','herokuevent-v1.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.core',
    'apps.events',
    'apps.logout',
    'apps.payment',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.authentication.MW_Authentication',
    'middleware.post_login.MW_PostLoginCommon',
]

ROOT_URLCONF = 'event_management.urls'

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

WSGI_APPLICATION = 'event_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

STRIPE_SECRET_KEY = 'sk_test_51I7dp1CrEfaSRzhzIq7W1MkaPNAFBB39xdrH1MEG1Du8rCZ79bGPFu18WqpS5er6R9P7qmQvCyeEziRdIAczOWRi00usmuKZE0'
STRIPE_PUBLISHABLE_KEY = 'pk_test_51I7dp1CrEfaSRzhzsmSeVwkasp9TQMqkIu8c6RkR1oEXyRCtkIp3y4zz1x18On8MPQADnSHR1sdHVEf9c7sRPhwC001RTx0q3d'
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'test.event.sayonetech@gmail.com'
EMAIL_HOST_PASSWORD = 'Test@123'
EMAIL_PORT = 587
EMAIL_FROM_NAME = 'Event_'
SITE_URL="http://127.0.0.1:8000/"
SITE_NAME="http://127.0.0.1:8000/"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
AUTH_USER_MODEL = 'core.Account'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
#production_----------
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')
MEDIA_URL = '/media/'
#-------------------
#local------
#STATIC_URL = '/static/'
#STATIC_ROOT = '/static/'
#STATICFILES_DIRS = (
 #   os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static'),
#)
#MEDIA_ROOT =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')
#MEDIA_URL = '/media/'
#---------
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)