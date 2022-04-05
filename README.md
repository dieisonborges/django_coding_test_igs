# Django Coding Test
The purpose of this coding test is to evaluate your skills using Python and the Django web
framework.

## The problem
The IGS team is growing every month and now we need to have some applications to
manage employee information, such as name, e-mail and department. As any application
written at IGS, It must have an API to allow integrations.

## Deliverables
"IGS-Software Manager" app must have:
* A django admin panel to manage employees` data.
* A Django API to list, add and remove employees.
* the code should be delivered to a github.com repository.

## API example (List)
Request:
```bash
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

Response:
```json
[
    {
        "name": "Felipe Morais",
        "email": "felipe.morais@igs-software.com.br",
        "department": "Tester"
    },
    {
        "name": "Tatiane Laura",
        "email": "tatiane.laura@igs-software.com.br",
        "department": "Developer"
    },
    {
        "name": "Mauricio Alegretti",
        "email": "mauricio.alegretti@igs-software.com.br",
        "department": "RH"
    }
]
```

# Employee Information API - employeeapi

## To run this project:
Tested on Mac-Os and Ubuntu 20.04

```bash
docker-compose up
```
Note: Do not use ctrl + c, because it may close the application.

## The project start in:
[http://0.0.0.0:8000/](http://0.0.0.0:8000/)

## To populate the tables Run:
```bash
docker-compose exec web python manage.py migrate
```

## To Create the First User:
```bash
docker-compose exec web python manage.py createsuperuser
```

## Is importante to security renew the django secret:
```bash
docker-compose exec web python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Note: All variables are in docker-compose.yml in web enviroment.

## If you Desiree add new app in API Run:
```bash
docker-compose exec web python manage.py startapp newapp
```

## To List All Employees (No Authenticated Required):

[/employee/](http://0.0.0.0:8000/employee/)

```bash
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

## To explore the API you can use this Postman collection:

[IGS_Employee_API.postman_collection.json](docs/IGS_Employee_API.postman_collection.json)

## To run the unit tests:
```bash
docker-compose exec web python manage.py test
```

## FAQ

### Postgress Sync
In case of Postgress problem due to container synchronization, run the build again:
```bash
docker-compose build
```
