# Test task

Test task - Employee administration


##  Instructions for use and launch app.

1. Configure virtual environment settings

    1.1 Create virtual environment and activate it
    
    ```bash
    virtualenv -p python3.8 .venv
   source .venv/bin/activate
    ```
    1.2 Install required libraries

    ```bash
    pip install -r requirements.txt
    ```

2. Configure database administration 
    
    2.1. install postgresql
    
    2.2. open shell prompt
    ```bash
    sudo su - postgres
    psql
    ```
    2.3. Run the following commands:
    ```postgresplsql
    CREATE DATABASE employee_db with encoding='UTF-8' LC_CTYPE='en_US.UTF-8' LC_COLLATE='en_US.UTF-8' TEMPLATE=template0;
    CREATE ROLE employee_user WITH PASSWORD 'qwerty123';
    GRANT ALL PRIVILEGES ON DATABASE employee_db to employee_user;
    ALTER ROLE employee_user LOGIN CREATEDB;
    ```

3. Migrate and seed the database and create super user

    ```bash
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py seeddatabase
    ```
   
    ```bash
    ./manage.py createsuperuser
   
   username:admin
   email:
   password:admin
    ```

4. Run the server and check it by opening localhost:8000 in web browser

    ```bash
    ./manage.py runserver
    ```
    
5. Test API documentation

    ```
    http://127.0.0.1:8000/api/docs/
    ```
