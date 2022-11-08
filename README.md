# gutendex

API created to test the functionalities of Gutendex API

## create a .env file with following data:
POSTGRES_DB=gutendex <br>
POSTGRES_USER=gutendex <br>
POSTGRES_PASSWORD=gutendex <br>
TIMEZONE=UTC <br>
POSTGRES_NAME=gutendex

## execute the following scripts:
1. docker-compose up
2. docker-compose exec api python manage.py migrate

## to see the api documentation go to:
http://localhost:8000/swagger

## to run the tests execute the following code
docker-compose exec api python manage.py test
