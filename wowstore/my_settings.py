# SECURITY WARNING: keep the secret key used in production secret!
MY_SECRET = {
    "SECRET_KEY" : 'django-insecure-mww(3x^#-*l7@5&8!5v@i(d+zmd$q-i6anceahe$zr_8x&2ax-'
}


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

MY_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wowstore',
        'USER': 'admin',
        'PASSWORD': '!Zxc846795',
        'HOST': 'mydatabase.crpiw2eagwlo.us-east-1.rds.amazonaws.com',
        'PORT':'3306',
        'OPTIONS':{
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}