# Show devices

Development tools:

- Django
- Django rest Framework

## How to run locally:

1. Clone the repository.
2. Enter in the folder.
3. Create an enviroment with Python 3.12.
4. Activate the enviroment.
5. Install the dependencies.
6. Run the migration.
7. Create a superuser
8. Run the server.

```
git clone git@github.com:ffabiorj/show-devices.git
cd show_devices
python3 -m venv .venv
sourch .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Using Docker compose
```
python contrib/env_gen.py
docker compose up --build
docker compose run web python manage.py migrate
docker compose run web python manage.py createsuperuser
```
#### If you use docker compose, remember to change the host to 0.0.0.0

### Endpoint to generate a login token:

Method post localhost:8000/api/v1/api/token

Body

```
{
    "email": "teste@teste.com",
    "password": "teste"
}
```

### Endpoint to create a device:

Method post localhost:8000/api/v1/devices/

Body

```
{
    "user": 1,
    "name": "test@fabio.com",
    "ip": "127.0.0.1",
    "is_active": true
}
```

To access these endpoints you need to send a token authorization "Bearer token".

### Endpoint to get all devices:

Method get localhost:8000/api/v1/devices/

Response:

```
[
{
    "name": "test",
    "ip": "127.0.0.1",
    "is_active": true
},
]

```

To test the api, use:

```
pytest
```
