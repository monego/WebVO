from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from fof.forms import FoFForm
from fof.models import FoFAlgorithm
from fof.tasks import RunFoFSerial
from resulttable.models import Execution

@csrf_protect
def fof(request):
    if request.method == 'POST':
        form = FoFForm(request.POST, request.FILES or None)
        if not form.is_valid():
            title = "Experiments %s" % (request.user)
            context = {
                "form": form,
                'title': title
            }
            return render(request, "fof/FoF.html", context)

        idAlg = request.POST.get('Algorithm')
        processos = request.POST.get('processos')
        kernels = request.POST.get('kernels')
        rperc = request.POST['Rperc']

        usuario = User.objects.get(username=request.user)
        alg = FoFAlgorithm.objects.get(idFoF=idAlg)

        execution = Execution(
            request_by=usuario.usuariofriends,
            algorithm = alg.nameFoF,
        )
        execution.save()

        #pega o arquivo de entrada:
        if(request.FILES):
            fileIn = request.FILES["Input"]
            execution.inputFile = fileIn
            execution.save()

            queryInputFile = (
                settings.MEDIA_ROOT +
                execution.inputFile.name.replace('./', '/')
            ).replace(' ', '\ ')

            queryOutputFile = queryInputFile
            queryOutputFile = queryOutputFile.replace('input', 'output')

            print("Query input file:" + queryInputFile)
            print("Query output file:" + queryOutputFile)

            outputFilePath = settings.MEDIA_ROOT + 'users/user_' + str(execution.request_by.usuario.id) + '/' + str(execution.id) + '/output-'
            logFilePath = settings.MEDIA_ROOT + 'users/user_' + str(execution.request_by.usuario.id) + '/' + str(execution.id) + '/log-'

        run = RunFoFSerial(alg.commandFoF, rperc, processos, kernels, execution.id, queryInputFile, outputFilePath, logFilePath)

        return HttpResponseRedirect(reverse('experiments'))

    form = FoFForm(request.POST or None)
    title = "Experiments %s" % (request.user)
    context = {
        "title": title,
        "form": form
    }

    return render(request, 'fof/FoF.html', context)

def about(request):
    query_results = FoFAlgorithm.objects.all()
    return render(request, 'fof/about.html', {"results" : query_results})
