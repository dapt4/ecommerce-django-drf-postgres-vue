# ecommerce-django-drf-postgres-vue

![store](https://github.com/dapt4/ecommerce-django-drf-postgres-vue/assets/67972962/c4a267f0-c27b-4ab2-9dbd-8d862c6423f7)

## Setup the backend

go to backend folder

`$ cd backend_django`

create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requeriments

`$ pip install -r requirements.txt`

install postgresql, login and create the database

`CREATE DATABASE <yourDBname>;`

create a .env file in the root folder

`$ touch .env`

and add your postgresql credentials and the app SECRET_KEY to .env file

>ENV_SECRET_KEY="{add a secret key like bhajfbkjhawbdkjhabdjh}"\
ENV_NAME='{yourDBname}'\
ENV_HOST='{your host or localhost}'\
ENV_PORT='{your db port or 5432}'\
ENV_USER='{your db user}'\
ENV_PASSWORD='{your db password}'

run the command:

`python manage.py makemigrations`

`python manage.py migrate`

finally the project run with: 

`$ python manage.py runserver`

open your RESTCLIENT (like postman) in: 

`GET or POST http://localhost:8000/product`\
`GET or PUT or DELETE http://localhost:8000/product/<int:id>`\
`POST http://localhost:8000/order`

## Setup the frontend

go to frontend folder and

`$ cd frontend_vue`

install dependencies

`$ npm install`

and run server

`$ npm run serve`

open your browser in:

`http://localhost:8080/`
