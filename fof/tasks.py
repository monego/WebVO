from resulttable.models import Execution
from celery.utils.log import get_task_logger
from celery.decorators import task
import requests
import os
import time

logger = get_task_logger(__name__)


@task(bind=True, name="FoFSerial")
def RunFoFSerial(self, command, rperc, processos, kernels, ide, input, output, logfile):

    print("\nExecutando o exp %s, algoritmo: %s" % (ide, command))

    start = time.time()
    os.system(command + " " + output + " " + str(ide) + " " + input + " " + rperc + " " + processos + " " + kernels + " > " + logfile)
    dur = time.time() - start

    exec = Execution.objects.get(pk=ide)
    exec.outputFile = output+"Groups_" + str(ide)
    exec.logFile = logfile
    exec.status = 3
    exec.save()

    #with open(logfile, 'w+') as f:
    #    f.write("")

    out = {'file': open(output+"Groups_"+str(ide), 'rb')}
    data = {'id': str(ide), 'time': dur}
    log = {'log': open(logfile, 'r')}

    requests.post('http://127.0.0.1:8000/experiments/result', files=out, data=data)
    requests.post('http://127.0.0.1:8000/experiments/log', files=log)