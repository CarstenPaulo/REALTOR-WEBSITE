import os
from pathlib import Path
from decouple import config
import cloudinary
import cloudinary_storage

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-ke)6i+^q3=c#7sye08)_&(h0_kif7e-5h_72uqd(99yjh0esdh'


DEBUG = False


ALLOWED_HOSTS = ['127.0.0.1','*.douglasrodriguesimoveis.com.br','www.douglasrodriguesimoveis.com.br','douglasrodriguesimoveis.com.br','corvobrancoimoveis.herokuapp.com']


  
INSTALLED_APPS = [
    'django.contrib.admin', 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    'listagens',
    'corretor',
    'django.contrib.humanize',
    'embed_video',
    'crispy_forms',
    'cloudinary',
    'cloudinary_storage',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


ROOT_URLCONF = 'project.urls'



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

WSGI_APPLICATION = 'project.wsgi.application'





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'dc8qffh2dc6npd',

        'HOST':'ec2-54-160-109-68.compute-1.amazonaws.com',
        'PORT':'5432',

        'USER':'vzkjkxftvgtsku',

        'PASSWORD':'8bf1733e40b898679817974547b91883b95cd831864947f67057230bf5c8d36c',
        
    }
}

#postgres://vzkjkxftvgtsku:8bf1733e40b898679817974547b91883b95cd831864947f67057230bf5c8d36c@/dc8qffh2dc6npd


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




LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'project/static')
]




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CRISPY_TEMPLATE_PACK = 'bootstrap4'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'corvobrancoimobiliaria@gmail.com'
EMAIL_HOST_PASSWORD = 'eeicpdmdiqbosvpj'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'corvobrancoimobiliaria@gmail.com'



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME', default="corvobrancoimoveis"),
    'API_KEY': config('API_KEY', default="985696424584293"),
    'API_SECRET': config('API_SECRET', default="D9CXFQF1sXw7RKg7i_IkDyn7Ub0"),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


LOGOUT_REDIRECT_URL  = 'index'