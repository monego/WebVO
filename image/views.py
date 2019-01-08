from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from image.forms import WaveletForm
from image.tasks import WaveletExperiment
from resulttable.models import Execution
from webfriends.views import home


@csrf_protect
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

        d_User = User.objects.get(username=request.user)
        wavelet = request.POST.get("Wavelet")
        method = request.POST.get("Method")

        if method == 'visushrink':
            method = 'VisuShrink'
        else:
            method = 'BayesShrink'

        execution = Execution(
            request_by=d_User.usuariofriends
        )

        execution.save()

        if request.FILES:
            fileIn = request.FILES["Input"]
            execution.inputFile = fileIn
            execution.save()
            queryInputFile = (
                settings.MEDIA_ROOT +
                execution.inputFile.name.replace('./', '/')
            ).replace(' ', '\ ')
            queryOutputFile = queryInputFile
            queryOutputFile = queryOutputFile.replace('input', 'output')

        # Run Experiment

        outputFilePath = settings.MEDIA_ROOT + 'users/user_' + \
            str(execution.request_by.usuario.id) + \
            '/' + str(execution.id) + '/output.' + request.POST.get("Format")

        print(outputFilePath)
        
        run = WaveletExperiment.delay((wavelet, method), request.user.email, queryInputFile, outputFilePath, execution.id)

        return HttpResponseRedirect(reverse('home'))

    form = WaveletForm(request.POST or None)

    title = "Experiments %s" % (request.user)
    context = {
        "title": title,
        "form": form
    }

    return render(request, "wavelet.html", context)
