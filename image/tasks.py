from celery.utils.log import get_task_logger
from webfriends.celery import app
import skimage.restoration as skr

logger = get_task_logger(__name__)

@app.task(name="ImageExperiment")
def ImageExperiment(request):

    server_url = 'http://127.0.0.1:8000'

    if request[0] == 'wavelet':
        d = skr.denoise_wavelet(request[1], wavelet=request[2], method=request[3])


    r = requests.post(server_url + 'experiments/result',
                      files=files,
                      data=data)
