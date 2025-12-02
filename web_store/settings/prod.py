from pathlib import Path
from decouple import config,Csv
from .base import *

DEBUG = config("DEBUG" , cast=bool , default=True)
ALLOWED_HOSTS += ["127.0.0.1" , "localhost"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("zhoobin_store_db" , default="zhoobin_store_db") ,
        'USER' : config("postgres" , default="postgres") ,
        'PASSWORD' : config("postgres" , default="postgres") ,
        'HOST' : config("localhost" , default="localhost") ,
        'PORT' : config("5432" , default="5432") ,
    }
}