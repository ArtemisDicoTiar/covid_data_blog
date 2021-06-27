from django.db import models


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
    index = models.BigIntegerField(db_column='index')
    ISO_code = models.TextField(db_column='ISO code', primary_key=True)
    Date = models.TextField()
    Daily_change_in_cumulative_total = models.FloatField(db_column='Daily change in cumulative total')
    Cumulative_total = models.FloatField(db_column='Cumulative total')
    Cumulative_total_per_thousand = models.FloatField(db_column='Cumulative total per thousand')
    Daily_change_in_cumulative_total_per_thousand = models.FloatField(db_column='Daily change in cumulative total per thousand')
    seven_day_smoothed_daily_change = models.FloatField(db_column='7-day smoothed daily change')
    seven_day_smoothed_daily_change_per_thousand = models.FloatField(db_column='7-day smoothed daily change per thousand')
    Short_term_positive_rate = models.FloatField(db_column='Short-term positive rate')
    Short_term_tests_per_case = models.FloatField(db_column='Short-term tests per case')

    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_testing_data'


class OWID_testing_meta(models.Model):
    index = models.BigIntegerField(db_column='index')
    ISO_code = models.TextField(db_column='ISO code', primary_key=True)
    Date = models.TextField()
    Entity = models.TextField()
    Source_URL = models.TextField(db_column='Source URL')
    Source_label = models.TextField(db_column='Source label')
    Number_of_observations = models.FloatField(db_column='Number of observations')
    Cumulative_total = models.FloatField(db_column='Cumulative total')
    Cumulative_total_per_thousand = models.FloatField(db_column='Cumulative total per thousand')
    Daily_change_in_cumulative_total = models.FloatField(db_column='Daily change in cumulative total')
    Daily_change_in_cumulative_total_per_thousand = models.FloatField(db_column='Daily change in cumulative total per thousand')
    seven_day_smoothed_daily_change = models.FloatField(db_column='7-day smoothed daily change')
    seven_day_smoothed_daily_change_per_thousand = models.FloatField(db_column='7-day smoothed daily change per thousand')
    Short_term_positive_rate = models.FloatField(db_column='Short-term positive rate')
    Short_term_tests_per_case = models.FloatField(db_column='Short-term tests per case')
    General_source_label = models.TextField(db_column='General source label')
    General_source_URL = models.TextField(db_column='General source URL')
    Short_description = models.TextField(db_column='Short description')
    Detailed_description = models.TextField(db_column='Detailed description')

    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_testing_meta'


class OWID_vaccination_data(models.Model):
    location = models.TextField()
    iso_code = models.TextField(primary_key=True)
    date = models.TextField()
    total_vaccinations = models.FloatField()
    people_vaccinated = models.FloatField()
    people_fully_vaccinated = models.FloatField()
    daily_vaccinations_raw = models.FloatField()
    daily_vaccinations = models.FloatField()
    total_vaccinations_per_hundred = models.FloatField()
    people_vaccinated_per_hundred = models.FloatField()
    people_fully_vaccinated_per_hundred = models.FloatField()
    daily_vaccinations_per_million = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_vaccination_data'


class OWID_vaccination_meta(models.Model):
    iso_code = models.TextField(primary_key=True)
    location = models.TextField()
    vaccines = models.TextField()
    last_observation_date = models.TextField()
    source_name = models.TextField()
    source_website = models.TextField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_vaccination_meta'
