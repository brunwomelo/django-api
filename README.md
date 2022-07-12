# IGS Software Manager

To run this app correctly, we first need to create an virtual env, this can be done via command line `python3.9 -m venv venv`, enter the virtual env with `source venv/bin/activate`, and then we can install the dependencies with `pip install -r requirements.txt`.
This app was built using PSQL Database, and to activate the db, we should make and `.env` file, with the fields listed bellow
```
DEBUG=FALSE #use True for development
SECRET_KEY=django_secret_key
HOST=dh_host
USER=db_user
PASSWORD=db_password
PORT=db_port
NAME=db_name
```

For the first time running the application, we should run the commands `python3 manage.py makemigrations` and `python3 manage.py migrate`, these commands ensure that our database will be updated with the models created in this program.
It's also adviseble to create a super user with `python3 manage.py createsuperuser`, this will allow us to access the control panel, in the url `/admin/` and also access our models and create new data. This also can be done with the post request for authenticated user in `/employee/` and `/department/`
Once the .env file is created, we can run the program with ``python3 manage.py runserver`, this should put the application to the default port 127.0.0.1:8000


