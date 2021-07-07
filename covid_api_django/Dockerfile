# Base python image Build
FROM python:3.9-buster AS builder

WORKDIR /covid_api_django
COPY requirements.txt /covid_api_django/

RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

# Django application image build
FROM builder AS deployer
WORKDIR /covid_api_django
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

COPY . .

# Deploy
EXPOSE 8000
RUN python manage.py migrate && python manage.py collectstatic --noinput
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]