from .settings import*
from .settings import BASE_DIR
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] 

# Application definition


MIDDLEWARE = [
     


    "django.middleware.security.SecurityMiddleware",
     'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]




# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
   # 'default': {
      #  'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
   # }
#}
c_s = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
pairs = [pair.split("=") for pair in c_s.split(" ")]
p_m = {pair[0]: pair[1] for pair in pairs}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': p_m["dbname"],
        'HOST': p_m['host'],
        'USER': p_m["user"],
        'PASSWORD':p_m["password"] ,
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATIC_URL = 'static/'



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'