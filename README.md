# Web Friends Portal

Development of the project:\
"Web Platform for Experiments with the Friends-of-Friends Hybrid Parallel Algorithm for Astronomical Objects Classification"\
\
Original application developed by Otávio Madalosso: https://github.com/Madalosso/TG/tree/master/Django%20Proj/webfriends 

## Summary

* [Running Local](#running-local)
* [Using Heroku](#using-heroku)
* [References](#references)

-----

## Running Local
Using an virtual environment.

1. Create new virtual environment: 
``` bash 
$ sudo python2 -m pip install virtualenv
($  virtualenv --version)
$ virtualenv myenv
```
2. Activate it and create an requirements log: 
``` bash 
$ source myvenv/bin/activate
$ pip freeze > requirements.txt
($ pip list)
```
<!---  3.0 - Create project inside the virtualenv (in case of new project): $ django-admin startproject projname . --->

3. Install all the packages which the project will use:
``` bash 
$ pip install Django==1.8	
$ pip install Celery==3.1.18
$ pip install django-registration-redux==1.4
$ pip install --upgrade django-crispy-forms==1.6.1
$ pip install django-jsonview==1.0.0
$ wget http://download.redis.io/releases/redis-3.0.0.tar.gz
$ tar xzvf redis-3.0.0.tar.gz
$ cd redis-3.0.0
$ make
$ pip install django-celery
$ pip install redis
$ pip install pipenv
$ pipenv install requests==2.8.1
```
4. For an existing git project just clone it inside the virtual environment 

5. Start the Django app:

``` bash
to start redis server: $ /redis-3.0.0/src/redis-server
to start django server: $ ./manage.py runserver
to start celery worker: $ celery -A webfriends worker -l info
```
- **Attention!** Changes are needed in settings, experiments and tasks files.

## Using Heroku

1. Create an Heroku application 
2. Create new virtual environment
3. Activate it and create an requirement log
4. Create runtime.txt with:\
python-2.7.14 - by default Heroku uses latest python version
5. Install all the packages the application need plus:
```bash
$ pip install gunicorn
$ pip install gevent
$ pip install whitenoise
$ pip install dj-database
```
<!--- move redis-3.0.0/src/redis-server to the project root --->

6. For an existing git project just clone it inside the virtual environment 
<!---Put the ./webfriends/ folder inside project root--->
7. Do some chances in settings and tasks files.

<!--- (change the IP and user)
Changes in tasks.py - 
    server_url = 'http://0.0.0.0'
    if 'PORT' in os.environ:
       server_url += ':' + os.environ['PORT']
       print("Port " + os.environ['PORT'])
    
    print("\n Executando o exp %s, algoritmo: %s" % (ide, execution))
    os.system("mkdir " + str(ide))
    os.system("wget https://webfriends.herokuapp.com/media/users/user_1/" + 
         str(ide) + "/input" + " -O ./" + str(ide) + "/input") 
    start = time.time()
    os.system(execution + " " + str(ide) + "/input > " + str(ide) + "/output")
    dur = time.time() - start  
    
	  $ python manage.py migrate
    $ ./manage.py syncdb --->

8. $ pip freeze > requirements.txt
  
9. Basic commands:
```bash
$ git init
$ heroku git:remote -a appname
$ git add .
$ git commit -am "text"
$ git push heroku master
$ heroku open
$ heroku login
$ heroku logs
$ heroku restart
$ heroku config:set WEB_CONCURRENCY=(1-3)
$ heroku labs:enable log-runtime-metrics 
```

9 - Change Procfile to work with Celery + Redis + Gunicorn in 1 web dyno:

https://drdaeman.github.io/heroku-djcelery-example/

http://heyman.info/2012/dec/6/heroku-multiple-processes-single-dyno-with-foreman/ (used here)

<!--- Procfile file: 
web: env > .env; env GEM_HOME=$HOME/.ruby-gems env PATH=$PATH:$HOME/.ruby-gems/bin foreman start -f ProcfileFree
ProcfileFree file: 
web: sh -c 'cd webfriends/ && gunicorn webfriends.wsgi:application --worker-class gevent --log-file - --log-level debug'
redis: ./redis-server
celery: sh -c 'cd webfriends/ && celery -A webfriends worker -l info' 
Use:
$ celery -A proj worker -l info -Ofair
With this option enabled the worker will only write to processes that are available for work, disabling the prefetch behavior
Add in settings.py to prevent never-ending tasks:--->


## References
- https://devcenter.heroku.com/articles/python-gunicorn
- https://devcenter.heroku.com/articles/django-asset
- https://devcenter.heroku.com/articles/gitignore
- https://devcenter.heroku.com/articles/django-app-configuration
- https://devcenter.heroku.com/articles/deploying-python
- https://devcenter.heroku.com/articles/celery-heroku
