from django.db import models


# Create your models here.
class COVID_Cases(models.Model):
    CountryCode = models.TextField(primary_key=True)
    ContinentName = models.TextField()
    SubdivisionCode = models.TextField()
    date = models.DateField()
    confirmed = models.FloatField()
    deaths = models.FloatField()
    recovered = models.FloatField()
    removed = models.FloatField()
    active = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'COVID_Cases'


class COVID_Cases_prediction(models.Model):
    predicted = models.DateField()
    CountryCode = models.TextField(primary_key=True)
    ContinentName = models.TextField()
    date = models.DateField()
    confirmed_prediction = models.BigIntegerField()
    deaths_prediction = models.BigIntegerField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'COVID_Cases_prediction'


class COVID_Cases_prediction_accuracy(models.Model):
    calculated = models.DateField()
    CountryCode = models.TextField(primary_key=True)
    ContinentName = models.TextField()
    yesterday_accuracy = models.FloatField()
    lastweek_accuracy = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'COVID_Cases_prediction_accuracy'


class Google_Mobility(models.Model):
    CountryName = models.TextField()
    CountryCode = models.TextField(primary_key=True)
    date = models.DateField()

    retail_and_recreation_percent_change_from_baseline = models.FloatField()
    grocery_and_pharmacy_percent_change_from_baseline = models.FloatField()
    parks_percent_change_from_baseline = models.FloatField()
    transit_stations_percent_change_from_baseline = models.FloatField()
    workplaces_percent_change_from_baseline = models.FloatField()
    residential_percent_change_from_baseline = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'Google_Mobility'


class OWID_health(models.Model):
    iso_code = models.TextField(primary_key=True)
    continent = models.TextField()
    date = models.DateField()
    total_cases = models.FloatField()
    new_cases = models.FloatField()
    new_cases_smoothed = models.FloatField()
    total_deaths = models.FloatField()
    new_deaths = models.FloatField()
    new_deaths_smoothed = models.FloatField()
    total_cases_per_million = models.FloatField()
    new_cases_per_million = models.FloatField()
    new_cases_smoothed_per_million = models.FloatField()
    total_deaths_per_million = models.FloatField()
    new_deaths_per_million = models.FloatField()
    new_deaths_smoothed_per_million = models.FloatField()
    reproduction_rate = models.FloatField()
    icu_patients = models.FloatField()
    icu_patients_per_million = models.FloatField()
    hosp_patients = models.FloatField()
    hosp_patients_per_million = models.FloatField()
    weekly_icu_admissions = models.FloatField()
    weekly_icu_admissions_per_million = models.FloatField()
    weekly_hosp_admissions = models.FloatField()
    weekly_hosp_admissions_per_million = models.FloatField()
    total_tests = models.FloatField()
    new_tests = models.FloatField()
    total_tests_per_thousand = models.FloatField()
    new_tests_per_thousand = models.FloatField()
    new_tests_smoothed = models.FloatField()
    new_tests_smoothed_per_thousand = models.FloatField()
    tests_per_case = models.FloatField()
    positive_rate = models.FloatField()
    tests_units = models.TextField()
    stringency_index = models.FloatField()
    population = models.FloatField()
    population_density = models.FloatField()
    median_age = models.FloatField()
    aged_65_older = models.FloatField()
    aged_70_older = models.FloatField()
    gdp_per_capita = models.FloatField()
    extreme_poverty = models.FloatField()
    cardiovasc_death_rate = models.FloatField()
    diabetes_prevalence = models.FloatField()
    female_smokers = models.FloatField()
    male_smokers = models.FloatField()
    handwashing_facilities = models.FloatField()
    hospital_beds_per_thousand = models.FloatField()
    life_expectancy = models.FloatField()
    human_development_index = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_health'


class OWID_mortality(models.Model):
    iso_code = models.TextField(primary_key=True)
    date = models.DateField()
    p_scores_all_ages = models.FloatField()
    p_scores_15_64 = models.FloatField()
    p_scores_65_74 = models.FloatField()
    p_scores_75_84 = models.FloatField()
    p_scores_85plus = models.FloatField()
    deaths_2020_all_ages = models.FloatField()
    average_deaths_2015_2019_all_ages = models.FloatField()
    deaths_2015_all_ages = models.FloatField()
    deaths_2016_all_ages = models.FloatField()
    deaths_2017_all_ages = models.FloatField()
    deaths_2018_all_ages = models.FloatField()
    deaths_2019_all_ages = models.FloatField()
    deaths_2010_all_ages = models.FloatField()
    deaths_2011_all_ages = models.FloatField()
    deaths_2012_all_ages = models.FloatField()
    deaths_2013_all_ages = models.FloatField()
    deaths_2014_all_ages = models.FloatField()
    deaths_2021_all_ages = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_mortality'


class OWID_testing_data(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_testing_data'


class OWID_testing_meta(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_testing_meta'


class OWID_vaccination_data(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_vaccination_data'


class OWID_vaccination_meta(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_vaccination_meta'


class UK_Cases(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'UK_Cases'


class UK_Cases_prediction(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'UK_Cases_prediction'


class UK_Cases_prediction_accuracy(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'UK_Cases_prediction_accuracy'
