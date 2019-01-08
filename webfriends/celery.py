# Configuração exemplo adaptada de
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

from celery import Celery
from django.conf import settings
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webfriends.settings')

app = Celery('webfriends')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name='tasks', force=True)

# app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks(related_name='tasks', force=True)
# app.conf.broker_url = 'redis://localhost:6379/0'

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))