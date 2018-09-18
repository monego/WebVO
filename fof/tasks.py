from .models import UsuarioFriends, Execution
from celery.utils.log import get_task_logger
# from celery.decorators import task
from webfriends.celery import app
import requests
import os
import time

logger = get_task_logger(__name__)


@app.task(name="RunExperiment")
def RunExperiment(execution, ide):

    server_url = 'http://127.0.0.1:8000'

    if 'PORT' in os.environ:
        server_url += ':' + os.environ['PORT']

    start = time.time()
    os.system(execution)
    dur = time.time() - start

    files = {'file': str("/"+str(ide) + "/output")}
    path = str(str(ide)+"/output")

    files = {'file': open(path, 'rb')}
    data = {'id': str(ide), 'time': dur}
    r = requests.post('http://127.0.0.1:8000' + '/experiments/result',
                      files=files,
                      data=data)

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
