# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6=-4wjr$ufs4&#1re)3@$f5h27i&*ngxsqbwa7u@juhuc8_*lp'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kanban',
        'USER': 'alexchescheir',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
