# Configuração exemplo adaptada de
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webfriends.settings')

app = Celery('webfriends')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
# app.conf.broker_url = 'redis://localhost:6379/0'

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
