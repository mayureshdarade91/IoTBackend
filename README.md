#### IoT Backend

### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: 
    ```
        virtualenv venv; \
        . venv/bin/activate; \
        pip install -r requirements.txt;
    ```
    
    To run application:
    ```
        . venv/bin/activate; \
	    python manage.py run
    ```

Make sure to run the initial migration commands to update the database.
    ```
    > python manage.py db init
    
    > python manage.py db migrate --message 'initial database migration'

    > python manage.py db upgrade
    ```

### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"
