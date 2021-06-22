FROM python:3.9

RUN mkdir /covid_api_django
WORKDIR /covid_api_django

ADD requirements.txt /covid_api_django/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "8000"]