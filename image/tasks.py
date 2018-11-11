from celery.utils.log import get_task_logger
from webfriends.celery import app
import simplejson as json
import codecs
import numpy as np
import skimage.io as skio
import skimage.restoration as skr

logger = get_task_logger(__name__)

@app.task(bind=True, name="Wavelet")
def WaveletExperiment(self, request, user_email, inputfile, outputfilepath):

    server_url = 'http://127.0.0.1:8000'

    img_dejson = skio.imread(inputfile)
    
    d = skr.denoise_wavelet(img_dejson, wavelet=request[0], method=request[1])

    skio.imsave(outputfilepath, d)

        # result = d.tolist()
        # file_path = "/tmp/file.json"
        # json.dump(result, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)

        # result_json = codecs.open(file_path, 'r', encoding='utf-8').read()
        # return result_json

#    r = requests.post(server_url + 'experiments/result',
#                      files=files,
#                      data=data)

    #send_mail(
    #    '[Observatório Virtual] Tarefa concluída',
    #    'A tarefa identificada pelo número ', ide, ', do aplicativo Imagens, foi concluída. Clique aqui para fazer o download do resultado.',
    #    'anawebfof@gmail.com',
    #    [user_email],
    #    fail_silently=False,
    #)
