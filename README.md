# Public chat room

Django application - public chat room(only RESTful API).

## Heroku
[https://testtaskchatroom.herokuapp.com/](https://testtaskchatroom.herokuapp.com/)

## REST API endpoints
Swagger documentation

`https://testtaskchatroom.herokuapp.com/`

API root

`https://testtaskchatroom.herokuapp.com/api/`

GET: messages list; POST: create message

`https://testtaskchatroom.herokuapp.com/api/messages/`

Get message by id, id example: 5

`https://testtaskchatroom.herokuapp.com/api/messages/id`

Paging example:

`https://testtaskchatroom.herokuapp.com/api/messages/?page=2`

## Getting Started
1. Install requirements

`pip install -r requirements.txt`

2. Database settings

Edit .env file 

### Postgres

`DB_NAME=chat`

`DB_USER=admin`

`DB_PASSWORD=1`

### Other settings
`SECRET_KEY=your secret key`

### Migrations
`python manage.py makemigrations`

`python manage.py migrate`

### Start project

`python manage.py runserver`

### Running the tests
`python manage.py test`
