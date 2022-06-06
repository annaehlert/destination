# Destination app
Destination app is created for connecting specific clients with their orders for a ride so it is easy to manage it. 
To start this app you need to:
1. download below repo.
2. create virtualenv on your computer. 
3. Download requirements.txt (with command pip install -r requirements.txt). 
4. Then you need to run below commands:
python manage.py makemigrations
python manage.py migrate
5. After all these steps you can run:
python manage.py runserver
and start to work.
If you want to use Django admin:
6. python manage.py createsuperuser
7. Enter your desired username, email and password.
8. After command 
python manage.py runserver and going to "admin/" endpoint you will be able
to login and work on data in database.
Technologies:
Python 3.8, Django 4.0.5, Bootstrap, sqlite3



