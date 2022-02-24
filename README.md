#### IoT Backend

### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: 
        virtualenv venv; \
        . venv/bin/activate; \
        pip install -r requirements.txt;
    
    To run application:
        . venv/bin/activate; \
	    python manage.py run

Make sure to run the initial migration commands to update the database.

    > python manage.py db init
    
    > python manage.py db migrate --message 'initial database migration'

    > python manage.py db upgrade

### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

### Sample CURL Req ####

    GET : /user

    curl -X 'GET' \
    'http://127.0.0.1:5000/user/' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX'


    POST : /user

    curl -X 'POST' \
    'http://127.0.0.1:5000/user/' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX' \
    -H 'Content-Type: application/json' \
    -d '{
    "email": "abc1@gmail.com",
    "username": "abc1",
    "password": "11111"
    }'


    POST : /auth/login

    curl -X 'POST' \
    'http://127.0.0.1:5000/auth/login' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX' \
    -H 'Content-Type: application/json' \
    -d '{
    "email": "abc1@gmail.com",
    "password": "11111"
    }'


    POST : /auth/logout

    curl -X 'POST' \
    'http://127.0.0.1:5000/auth/logout' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX' \
    -d ''


    GET : /device/

    curl -X 'GET' \
    'http://127.0.0.1:5000/device/' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX'


    POST : /device/

    curl -X 'POST' \
    'http://127.0.0.1:5000/device/' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX' \
    -H 'Content-Type: application/json' \
    -d '{
    "name": "Dev2",
    "org_id": 1
    }'


    GET ​: /device​/{name}

    curl -X 'GET' \
    'http://127.0.0.1:5000/device/Dev2' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX'


    PUT : /device/{name}

    curl -X 'PUT' \
    'http://127.0.0.1:5000/device/Dev2' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX' \
    -H 'Content-Type: application/json' \
    -d '{
    "name": "Dev3",
    "org_id": 1
    }'



    GET : /sensor/

    curl -X 'GET' \
    'http://127.0.0.1:5000/sensor/' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX'


    POST : /sensor/

    curl -X 'POST' \
    'http://127.0.0.1:5000/sensor/' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX' \
    -H 'Content-Type: application/json' \
    -d '{
    "name": "Vibration",
    "device_id": 1
    }'

    GET : /sensor/{device_id}

    curl -X 'GET' \
    'http://127.0.0.1:5000/sensor/1' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX'


    GET : /sensor_data/

    curl -X 'GET' \
    'http://127.0.0.1:5000/sensor_data/' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX'

    
    POST : /sensor_data/

    curl -X 'POST' \
    'http://127.0.0.1:5000/sensor_data/' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX' \
    -H 'Content-Type: application/json' \
    -d '{
    "sensor_id": 2,
    "sensor_data": 40
    }'


    POST : /sensor_data/filter_data

    curl -X 'POST' \
    'http://127.0.0.1:5000/sensor_data/filter_data' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX' \
    -H 'Content-Type: application/json' \
    -d '{
    "sensor_id": 1,
    "from": "2022-02-24T12:21:30.392390",
    "to": "2022-02-24T12:21:40.392390"
    }'


    GET : /sensor_data/{sensor_id}

    curl -X 'GET' \
    'http://127.0.0.1:5000/sensor_data/1' \
    -H 'accept: application/json' \
    -H 'Authorization: XXXXX'