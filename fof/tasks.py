from resulttable.models import Execution
from webfriends.models import UsuarioFriends
from celery.utils.log import get_task_logger
from celery.decorators import task
import requests
import os
import time

logger = get_task_logger(__name__)


@task(bind=True, name="FoFSerial")
def RunFoFSerial(self, command, rperc, ide, input, output, id):

    print("\nExecutando o exp %s, algoritmo: %s" % (ide, command))
    print(output)
    #Running FoF
    start = time.time()
    os.system(command + " " + input + " " + rperc + " > " + output)
    dur = time.time() - start

    exec = Execution.objects.get(pk=ide)
    exec.outputFile = output
    exec.save()

    files = {'file': open(output, 'rb')}
    data = {'id': str(ide), 'time': dur}

    r = requests.post('http://127.0.0.1:8000/experiments/result', files=files, data=data)

    print(r.status_code, r.reason)

@task(name="RunExperiment")
def RunExperiment(command, ide):
    server_url = 'http://127.0.0.1:8000'

    print("\nExecutando o experimento %s %s" % (command, ide))
    os.system("mkdir " + str(ide))
    os.system("wget " + server_url + "/experiments/downloadInputFile?id=" + str(ide) + " -O ./" + str(ide) + "/input")

    start = time.time()
    # os.system(execution + " " + str(ide) + "/input > " + str(ide) + "/output")
    os.system(command + " > " + str(ide) + "/output")
    dur = time.time() - start

    print("Duração: " + dur)

    files={'file': str("/"+str(ide) + "/output")}
    path = str(str(ide)+"/output")
    print(path)
    files = {'file': open(path, 'rb')}
    data = {'id':str(ide),'time':dur}
    r = requests.post('http://127.0.0.1:8000/' + 'experiments/result', files=files, data=data)
    print(r.status_code, r.reason)
           # execution.status = 2
           # execution.save()
           # start = time.time()
           # os.system(query)
           # dur = time.time() - start
           # print dur
           # execution.status = 3
           # user = execution.request_by
           # user.notes.add(nota)
           # user.save()
           # execution.time = dur
           # execution.outputFile = queryOutputFile
           # execution.save()