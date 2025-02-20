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
6. Execute the env_gen.
7. Run the migration.
8. Run the server.

```
git clone git@github.com:ffabiorj/show-devices.git
cd show_devices
python3 -m venv .venv
sourch .venv/bin/activate
pip install -r requirements.txt
python env_gen.py
python manage.py migrate
python manage.py runserver
```


### Endpoint to create a login:

Method post localhost:8000/api/v1/register/

Body

```
{
    "email": "teste@teste.com",
    "password": "teste"
}
```

### Endpoint to generate a login token:

Method post localhost:8000/api/v1/api/token

Body

```
{
    "email": "teste",
    "password": "teste"
}
```

### Endpoint to create a device:

Method post localhost:8000/api/v1/devices/

Body

```
{
    "name": "test",
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
{
    "name": "test2",
    "ip": "127.0.0.11",
    "is_active": true
}
]

```


## How to execute tests:

1. To test the api, use:

```
python manage.py test
```
