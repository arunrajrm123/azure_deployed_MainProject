import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS=[os.environ["WEBSITE_HOSTNAME"]]
CSRF_TRUSTED_ORIGINS=["https://"+os.environ["WEBSITE_HOSTNAME"]]
DEBUG=False

MIDDLEWARE = [
     


    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware "
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


STATICFILES_STORAGE='whitenoise.storage.CompressedmanifeststaticFilesstorage'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
connection_strings=os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parameters={pair.split("="):pair.split("=")[1] for pair in connection_strings.split(" ")}

DATABASES={
    "default":{
        'ENGINE':"django.db.backends.postgresql",
        "NAME":parameters['dbname'],
        "HOST":parameters['host'],
        "USER":parameters['user'],
        "PASSWORD":parameters['password'],
    }
}