# Web Friends Portal

Development of the project:\
"Web Platform for Experiments with the Friends-of-Friends Hybrid Parallel Algorithm for Astronomical Objects Classification"\
\
Original application developed by Otávio Madalosso: https://github.com/Madalosso/TG/tree/master/Django%20Proj/webfriends 

## Running Local

Using a virtual environment: first, install the Python 3 version of [pip](https://pypi.org/project/pip/) and [virtualenv](https://pypi.org/project/virtualenv/). Also install Redis, as it will be used as the Celery broker. On a Debian based system, type as root:

```bash 
$ apt install python3-pip virtualenv redis-server
```

1. Open the project's root folder and create a new virtual environment: 

``` bash 
$ virtualenv myenv -p "/usr/bin/python3" # Or whichever is the Python3 binary
```

2. Activate it:

``` bash 
$ source myvenv/bin/activate
```

3. Install all the packages that the project will use:

``` bash 
$ pip install django django-registration-redux django-crispy-forms django-jsonview celery redis scikit-image requests
```
4. For an existing git project just clone it inside the virtual environment 

5. Start the application:

``` bash 
$ redis-server # Start the Redis server
$ ./manage.py runserver # Start the Django app
$ celery -A webfriends worker --loglevel=DEBUG # Start the Celery worker
```

Finally, open http://localhost:8000 in a graphical web browser.

- **Attention!** Changes are needed in settings, experiments and tasks files.
