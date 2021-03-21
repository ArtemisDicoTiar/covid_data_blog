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
    'information_schema': 'INFORMATION_SCEMA',
    'covid_global_cumulative': 'covid',
    'covid_global_new': 'covid_new',

    'covid_uk_raw_ltla': 'covid_uk_raw_ltla',
    'covid_uk_raw_utla': 'covid_uk_raw_utla',
    'covid_uk_ltla': 'covid_uk_ltla',
    'covid_uk_utla': 'covid_uk_utla',

    'covid_dashboard': 'covid_dashboard',

    'owid_vac_test': 'covid_info_owid',
    'owid_pscore': 'owid_p_scores',
    'owid_region': 'owid_ext_infos',

    'google_mobility': 'google_mobility',

}