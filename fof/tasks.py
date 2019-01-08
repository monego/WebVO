from .models import UsuarioFriends
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from webfriends.celery import app
import os
import requests
import time

logger = get_task_logger(__name__)

@app.task(bind=True, name="RunExperiment")
def RunExperiment(self, execution, ide, user_email):

    server_url = 'http://127.0.0.1:8000'

    if 'PORT' in os.environ:
        server_url += ':' + os.environ['PORT']

    start = time.time()
    os.system(execution)
    dur = time.time() - start

    files = {'file': str("/"+str(ide) + "/output")}
    path = str(str(ide)+"/output")

    # files = {'file': open(path, 'rb')}
    # data = {'id': str(ide), 'time': dur}
    # r = requests.post('http://127.0.0.1:8000' + '/experiments/result',
    #                   files=files,
    #                   data=data)
    
    #send_mail(
    #    '[Observatório Virtual] Tarefa concluída',
    #    'A tarefa identificada pelo número ', ide, ', do aplicativo FoF, foi concluída. Clique aqui para fazer o download do resultado.',
    #    'anawebfof@gmail.com',
    #    [user_email],
    #    fail_silently=False,
    #)
    
    # print((r.status_code, r.reason))
    # execution.status = 2
    # execution.save()
    # start = time.time()
    # os.system(query)
    # dur = time.time() - start
    # print(dur)
    # execution.status = 3
    # user = execution.request_by
    # user.notes.add(nota)
    # user.save()
    # execution.time = dur
    # execution.outputFile = queryOutputFile
    # execution.save()
