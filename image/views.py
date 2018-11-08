from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from image.forms import WaveletForm
from image.tasks import WaveletExperiment
from resulttable.models import Execution
import codecs
import simplejson as json
import skimage.io as skio

def wavelet(request):

    if request.method == 'POST':

        form = WaveletForm(request.POST, request.FILES or None)

        if not form.is_valid():
            title = "Experiments %s" % (request.user)

            context = {
                "form": form,
                "title": title
            }

            return render(request, "wavelet.html", context)

        algorithm = request.POST['Algorithm']
        d_User = User.objects.get(username=request.user)
        inputFile = request.FILES["Input"]
        wavelet = request.POST.get("Wavelet")
        method = request.POST.get("Method")

        if method == 'visushrink':
            method = 'VisuShrink'
        else:
            method = 'BayesShrink'

        execution = Execution(
            request_by=d_User.usuariofriends,
            inputFile = request.FILES["Input"],
        )

        # JSONify Inputfile

        img = skio.imread(inputFile).tolist()
        file_path = "/tmp/file.json"
        json.dump(img, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)

        img_json = codecs.open(file_path, 'r', encoding='utf-8').read()

        # Run Experiment

        execution.save()

        run = WaveletExperiment.delay(('wavelet', img_json, wavelet, method), request.user.email)

        print(run)

#        img_result = json.loads(run)
#        img_dejson = np.array(img_result)

#        skio.imsave(img_dejson, "/tmp/final.jpg")

        return HttpResponseRedirect(reverse('home'))

    form = WaveletForm(request.POST or None)

    title = "Experiments %s" % (request.user)
    context = {
        "title": title,
        "form": form
    }

    return render(request, "wavelet.html", context)
