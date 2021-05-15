FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /covid_api_django
WORKDIR /covid_api_django

ADD requirements.txt /covid_api_django/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /covid_api_django/

#FROM python:3.7
#
#ENV PYTHONUNBUFFERED 1
#
#RUN mkdir /covid_api_django
#WORKDIR /covid_api_django
#
#ADD requirements.txt /covid_api_django/
#
#RUN pip install virtualenv
#RUN virtualenv covid_api_django
#
#WORKDIR ./covid_api_django
#RUN /bin/bash -c "source ./bin/activate"
#
#RUN pip install --upgrade pip
#RUN pip install -r ../requirements.txt
#
#ADD . /covid_api_django/