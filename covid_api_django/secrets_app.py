import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

DJANGO_SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
MARIA_DB_USER = os.getenv('MARIA_DB_USER')
MARIA_DB_PASSWORD = os.getenv('MARIA_DB_PASSWORD')
MARIA_DB_ADDRESS = os.getenv('MARIA_DB_ADDRESS')
MARIA_DB_PORT = os.getenv('MARIA_DB_PORT')
