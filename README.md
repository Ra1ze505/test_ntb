# Test for NTB
### Create at the root of the project file `.env`, example:
```
SECRET_KEY=change_me
DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_dev
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

### Create at the root of the project file `.env.db`, example:
```
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
POSTGRES_DB=hello_django_dev
```
### Up docker-compose:
```
docker-compose up
```
### You can view endpoints -> http://localhost:8000/swagger/

## Exec container:
```
docker-compose exec web /bin/bash
```
### Create superuser
```
python manage.py createsuperuser
```
