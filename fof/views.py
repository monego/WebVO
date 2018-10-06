from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from fof.forms import FoFForm
from fof.models import FoFAlgorithm, UsuarioFriends
from fof.tasks import RunExperiment
from webfriends.views import home

@csrf_protect
def fof(request):
    form = FoFForm(request.POST or None)
    # if form.is_valid():
    #     algorithm = request.POST.get('FoFAlgorithm')
    #     d_User = User.objects.get(username=request.user)
    #     alg = FoFAlgorithm.objects.get(nameAlg=algorithm)
    #     execution = FoF(
    #         request_by=d_User.usuariofriends,
    #         algorithm=alg,
    #     )

    #     execution.rperc = request.POST["Rperc"]
    #     execution.save()

    #     if (request.FILES):
    #         fileIn = request.FILES["Input"]
    #         execution.inputFile = fileIn
    #         execution.save()
    #         queryInputFile = (
    #             settings.MEDIA_ROOT +
    #             execution.inputFile.name.replace('./', '/')
    #         ).replace(' ', '\ ')
    #         queryOutputFile = queryInputFile
    #         queryOutputFile = queryOutputFile.replace('input', 'output')
    #         query = alg.command + ' ' + queryInputFile + ' ' + execution.rperc + ' > ' + queryOutputFile

    #     else:
    #         query = execution.algorithm.command

    #     outputFilePath = './users/user_' + \
    #         str(execution.request_by.usuario.id) + \
    #         '/' + str(execution.id) + '/output'
    #     teste = RunExperiment.delay(query, execution.id)
    #     execution.save()
    #     title = "Experiments %s" % (request.user)

    #     return HttpResponseRedirect(reverse('home'))

    title = "Experiments %s" % (request.user)

    context = {
        "form": form,
        "title": title
    }
    return render(request, "FoF.html", context)

# @csrf_protect
# def fof1(request):
#     if request.method == 'POST':
#         form = FoFForm(request.POST, request.FILES or None)

#         if not form.is_valid():

#             title = "Experiments %s" % (request.user)
#             # form_html = render_crispy_form(form)
#             context = {
#                 "form": form,
#                 'title': title
#             }

#             return render(request, "FoF.html", context)

#         algorithm = request.POST.get('FoFAlgorithm')
#         d_User = User.objects.get(username=request.user)
#         alg = FoFAlgorithm.objects.get(nameAlg=algorithm)
#         execution = FoF(
#             request_by=d_User.usuariofriends,
#             algorithm=alg,
#         )

#         execution.rperc = request.POST["Rperc"]
#         execution.save()

#         if (request.FILES):
#             fileIn = request.FILES["Input"]
#             execution.inputFile = fileIn
#             execution.save()
#             queryInputFile = (
#                 settings.MEDIA_ROOT +
#                 execution.inputFile.name.replace('./', '/')
#             ).replace(' ', '\ ')
#             queryOutputFile = queryInputFile
#             queryOutputFile = queryOutputFile.replace('input', 'output')
#             query = alg.command + ' ' + queryInputFile + ' ' + execution.rperc + ' > ' + queryOutputFile

#         else:
#             query = execution.algorithm.command

#         outputFilePath = './users/user_' + \
#             str(execution.request_by.usuario.id) + \
#             '/' + str(execution.id) + '/output'
#         teste = RunExperiment.delay(query, execution.id)
#         execution.save()
#         title = "Experiments %s" % (request.user)

#         return HttpResponseRedirect(reverse('home'))

#     form = FoFForm(request.POST or None)
#     title = "Experiments %s" % (request.user)
#     context = {
#         "title": title,
#         "form": form
#     }

#     return render(request, "FoF.html", context)

