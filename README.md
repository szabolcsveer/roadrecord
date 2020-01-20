GUIDE

Packages Installed while working on this project

Package                   Version
------------------------- -------
astroid                   2.3.3
colorama                  0.4.3
Django                    2.2.3
django-crispy-forms       1.8.1  
django-unixtimestampfield 0.3.9
djangorestframework       3.11.0
isort                     4.3.21
lazy-object-proxy         1.4.3
mccabe                    0.6.1
pip                       19.2.3
psycopg2                  2.8.4
pylint                    2.4.4
pytz                      2019.3
setuptools                41.2.0
six                       1.13.0
sqlparse                  0.3.0
typed-ast                 1.4.0
virtualenv                16.7.9 
virtualenvwrapper-win     1.2.5
wrapt                     1.11.2

Environment used:
- Python: 3.7
- Django: 2.2.3
- PostgreSQL: 10


Once you forked the repository and installed all the dependencies 
You can create an admin user by using the 'python manage.py createsuperuser' command
then start the app by using the 'python manage.py runserver' command
By going to http://127.0.0.1:8000/admin url, you will be able to add instances of the
Auto and Partner models as well as set their relations
You may add 'POST' or delete 'DELETE or retrieve 'GET' data to/from the database using POSTMAN
in JSON format.
On http://127.0.0.1:8000/register you can register a new user, and then you can login on
http://127.0.0.1:8000/login 
If you visit http://127.0.0.1:8000/auto/:id you can look up that particular instance  

