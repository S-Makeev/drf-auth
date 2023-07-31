## LAB - Class 33

### Lab: Authentication & Production Server

#### Author: Slava Makeev

### Setup

>.env requirements: active

Install dependencies: [dependencies](requirements.txt)

### PORT
>localhost

How to initialize/run your application:

> docker compose run web python manage.py runserver


### Tests

How do you run tests?

>python3 manage.py test
 
 
 ### GET/REFRESH TOKENS:
 
{

    "refresh": <YOUR TOKEN>

    "access": <YOUR TOKEN>
}

### DB URL:

> http://localhost:8000/api/v1/artists/ 
