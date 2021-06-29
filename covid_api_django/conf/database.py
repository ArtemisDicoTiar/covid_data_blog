import secrets_app

DATABASE_INFOS = {
    'NAME': '',
    'ENGINE': 'django.db.backends.mysql',
    'USER': secrets_app.MARIA_DB_USER,
    'PASSWORD': secrets_app.MARIA_DB_PASSWORD,
    'HOST': secrets_app.MARIA_DB_ADDRESS,
    'PORT': secrets_app.MARIA_DB_PORT
}

DATABASE_NAMES = {
    'information_schema': 'INFORMATION_SCHEMA',
    'covid_base': 'covid',
    'covid_info': 'covid_info'
}