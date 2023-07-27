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

    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MDUwMzg0NiwiaWF0IjoxNjkwNDE3NDQ2LCJqdGkiOiI4OGMwZDM1NGIzZWQ0YzZlYTY3OTA4OTU2OTBjZmJiNSIsInVzZXJfaWQiOjF9.9hWx774f8asg4edjwflBXUasKI4dFaRx8MeadNadEKA",

    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwNDE3NzQ2LCJpYXQiOjE2OTA0MTc0NDYsImp0aSI6ImYzMGRlNTY0ZDYyNzQyN2RhOTZkMzMyZjgyYWJmY2ZhIiwidXNlcl9pZCI6MX0.k9TUDbvEjQ553vM6aWwvBlUk6SYqJQ_RbCB2ZTP_XSY"
}

### DB URL:

> http://localhost:8000/api/v1/artists/ 