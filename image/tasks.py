from celery.utils.log import get_task_logger
from resulttable.models import Execution
from webfriends.celery import app
import simplejson as json
import codecs
import numpy as np
import requests
import skimage.io as skio
import skimage.restoration as skr

logger = get_task_logger(__name__)

@app.task(bind=True, name="Wavelet")
def WaveletExperiment(self, request, user_email, inputfile, outputfilepath, logfilepath, ide):

    server_url = 'http://127.0.0.1:8000'
    print(outputfilepath)
    img_dejson = skio.imread(inputfile)

    func_kw = dict(wavelet=request[0], method=request[1])
    d = skr.cycle_spin(img_dejson, func=skr.denoise_wavelet, max_shifts=int(request[2]), func_kw=func_kw)

    skio.imsave(outputfilepath, d)

    with open(logfilepath, 'w+') as logfile:
        logfile.write("")

    output = {'image': open(outputfilepath, 'rb')}
    log = {'log': open(logfilepath, 'r')}

    requests.post(server_url + '/experiments/result',
                  files=output)

    requests.post(server_url + '/experiments/log',
                  files=log)

    exec = Execution.objects.get(pk=ide)
    exec.outputFile = outputfilepath
    exec.logFile = logfilepath
    exec.status = 3
    exec.save()

    #send_mail(
    #    '[Observatório Virtual] Tarefa concluída',
    #    'A tarefa identificada pelo número ', ide, ', do aplicativo Imagens, foi concluída. Clique aqui para fazer o download do resultado.',
    #    'anawebfof@gmail.com',
    #    [user_email],
    #    fail_silently=False,
    #)
