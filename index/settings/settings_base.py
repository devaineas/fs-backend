import os

SECRET_KEY = 'fwy)=0a4%nh!!8#&ni)%2_#t9-(*6g^62-mih#rsyd!$860g$$'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sites',

    # 3rd Party

    'taggit',
    'maintenance_mode',
    'crispy_forms',
    'graphene_django',
    'django_countries',
    #'rest_framework',
    #'rest_framework.authtoken',
    #'rest_auth',
    #'allauth',
    #'allauth.account',
    #'rest_auth.registration',
    'rest_framework',
    'corsheaders',

    # Own

    'core',

]

GRAPHENE = {
    'SCHEMA': 'index.schema.schema'
}


#SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
#   'django.middleware.csrf.CsrfViewMiddleware', Remove this since its useless since we use react, if u use html templates in django, you need to enable this back
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maintenance_mode.middleware.MaintenanceModeMiddleware',
]

ROOT_URLCONF = 'index.urls'

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
                'maintenance_mode.context_processors.maintenance_mode',
            ],
        },
    },
]

WSGI_APPLICATION = 'index.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TAGGIT_CASE_INSENSITIVE = True

# Maintenance mode settings

# if True admin site will not be affected by the maintenance-mode page
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True
# if True the staff will not see the maintenance-mode page
MAINTENANCE_MODE_IGNORE_STAFF = True
# if True the superuser will not see the maintenance-mode page
MAINTENANCE_MODE_IGNORE_SUPERUSER = True
# the template that will be shown by the maintenance-mode page
MAINTENANCE_MODE_TEMPLATE = '503.html'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''



# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}



AUTHENTICATION_BACKENDS = [
    'core.CustomUserAuthBackend.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
]

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'core.api.utils.jwt_response_handler'
}


REACT_SECRET_KEY = 'fMti-Q_yykNI7dRfW?`:o+1`IjkA[N5QJ0KvsM=G&=/{Dk*|-L!.AtX&"^[=<H]#'

AUTH_USER_MODEL = 'core.CustomUser'