docker stop covid_api
docker stop covid_api_django
docker rm covid_api
docker rm covid_api_django

#docker rmi covid_api_django_django_api

docker build -t covid_api_django ./

docker run --rm -d -it -h "localhost" -p 8000:8000 --name covid_api_django covid_api_django
