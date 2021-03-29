from .base import *

ALLOWED_HOSTS = ['elarnoldo.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'elarnoldo$newarnoldo',
        'USER': 'elarnoldo',
        'PASSWORD': 'mentirosomentiroso',
        'HOST': 'elarnoldo.mysql.pythonanywhere-services.com',
    }
}
