# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
# from .celery import app as celery_app

default_app_config = 'webfriends.apps.WebFriendsConfig'

__all__ = ('celery_app',)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
# app = Celery('proj')
# app.config_from_object('django.conf:settings', namespace='CELERY')
