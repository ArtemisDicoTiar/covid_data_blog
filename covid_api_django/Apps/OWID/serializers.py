from rest_framework import serializers

from Apps.OWID.models import *


class OWID_healthSerializer(serializers.ModelSerializer):
    class Meta:
        model = OWID_health
        fields = [
            # 'iso_code',
            'continent',
            'date',
            'total_cases',
            'new_cases',
            'new_cases_smoothed',
            'total_deaths',
            'new_deaths',
            'new_deaths_smoothed',
            'total_cases_per_million',
            'new_cases_per_million',
            'new_cases_smoothed_per_million',
            'total_deaths_per_million',
            'new_deaths_per_million',
            'new_deaths_smoothed_per_million',
            'reproduction_rate',
            'icu_patients',
            'icu_patients_per_million',
            'hosp_patients',
            'hosp_patients_per_million',
            'weekly_icu_admissions',
            'weekly_icu_admissions_per_million',
            'weekly_hosp_admissions',
            'weekly_hosp_admissions_per_million',
            'total_tests',
            'new_tests',
            'total_tests_per_thousand',
            'new_tests_per_thousand',
            'new_tests_smoothed',
            'new_tests_smoothed_per_thousand',
            'tests_per_case',
            'positive_rate',
            'tests_units',
            'stringency_index',
            'population',
            'population_density',
            'median_age',
            'aged_65_older',
            'aged_70_older',
            'gdp_per_capita',
            'extreme_poverty',
            'cardiovasc_death_rate',
            'diabetes_prevalence',
            'female_smokers',
            'male_smokers',
            'handwashing_facilities',
            'hospital_beds_per_thousand',
            'life_expectancy',
            'human_development_index',
        ]


class OWID_mortalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OWID_mortality
        fields = [
            # 'iso_code',
            'date',
            'p_scores_all_ages',
            'p_scores_15_64',
            'p_scores_65_74',
            'p_scores_75_84',
            'p_scores_85plus',
            'deaths_2020_all_ages',
            'average_deaths_2015_2019_all_ages',
            'deaths_2015_all_ages',
            'deaths_2016_all_ages',
            'deaths_2017_all_ages',
            'deaths_2018_all_ages',
            'deaths_2019_all_ages',
            'deaths_2010_all_ages',
            'deaths_2011_all_ages',
            'deaths_2012_all_ages',
            'deaths_2013_all_ages',
            'deaths_2014_all_ages',
            'deaths_2021_all_ages',
        ]


class OWID_testing_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OWID_testing_data
        fields = [
            # 'index',
            # 'ISO_code',
            'Date',
            'Daily_change_in_cumulative_total',
            'Cumulative_total',
            'Cumulative_total_per_thousand',
            'Daily_change_in_cumulative_total_per_thousand',
            'seven_day_smoothed_daily_change',
            'seven_day_smoothed_daily_change_per_thousand',
            'Short_term_positive_rate',
            'Short_term_tests_per_case',
        ]


class OWID_testing_metaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OWID_testing_meta
        fields = [
            # 'ISO_code',
            'Date',
            'Entity',
            'Source_URL',
            'Source_label',
            'Number_of_observations',
            'Cumulative_total',
            'Cumulative_total_per_thousand',
            'Daily_change_in_cumulative_total',
            'Daily_change_in_cumulative_total_per_thousand',
            'seven_day_smoothed_daily_change',
            'seven_day_smoothed_daily_change_per_thousand',
            'Short_term_positive_rate',
            'Short_term_tests_per_case',
            'General_source_label',
            'General_source_URL',
            'Short_description',
            'Detailed_description',
        ]


class OWID_vaccination_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OWID_vaccination_data
        fields = [
            'location',
            # 'iso_code',
            'date',
            'total_vaccinations',
            'people_vaccinated',
            'people_fully_vaccinated',
            'daily_vaccinations_raw',
            'daily_vaccinations',
            'total_vaccinations_per_hundred',
            'people_vaccinated_per_hundred',
            'people_fully_vaccinated_per_hundred',
            'daily_vaccinations_per_million',
        ]


class OWID_vaccination_metaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OWID_vaccination_meta
        fields = [
            # 'iso_code',
            'location',
            'vaccines',
            'last_observation_date',
            'source_name',
            'source_website',
        ]
