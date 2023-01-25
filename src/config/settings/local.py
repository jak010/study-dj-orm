from .base import  *


from .base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '9902',
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
        'ATOMIC_REQUESTS': True
        # 'TEST': { # 테스트를 django test로 할 거면 주석 해제 후 사용
        #     'CHARSET': 'utf8',
        #     'COLLATION': 'utf8_general_ci',
        # }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'sql': {
            '()': 'django_sqlformatter.SqlFormatter',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'sql',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}