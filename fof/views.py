from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from fof.forms import ExecutionForm
from fof.models import Execution, Algorithms, UsuarioFriends
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from jsonview.decorators import json_view
from crispy_forms.utils import render_crispy_form
from crispy_forms.helper import FormHelper
from .paginator import paginate
from fof.tasks import RunExperiment


def home(request):
    if not request.user.is_authenticated:
        title = "Welcome"
        context = {
            "title": title
        }
        return render(request, "welcome.html", context)
    else:
        # res = teste.delay()
        # print(res)
        title = "Welcome %s" % request.user
        print((request.user.id))
        executionList = Execution.objects.filter(
            request_by__usuario__id=request.user.id).order_by('-id')
        try:
            UserProf = UsuarioFriends.objects.get(usuario__id=request.user.id)
        except:
            print("Erro. Criando novo userProf")
            user = User.objects.get(id=request.user.id)
            UserProf = UsuarioFriends(usuario=user)
            UserProf.save()
            print("Criado novo UserProf")
        paginator = Paginator(executionList, UserProf.resultsPerPage)
        page = request.GET.get('page')
        if page is None:
            page = 1
        try:
            executions = paginator.page(page)
        except PageNotAnInteger:
            executions = paginator.page(1)
        except EmptyPage:
            executions = paginator.page(paginator.num_pages)  # da pra tratar
        if paginator.count == 0:
            data = None
        else:
            data = executions
        pageI = paginate(page, paginator)
        context = {
            "title": title,
            "data": data,
            "pagesIndex": pageI,
        }
        return render(request, "home.html", context)


def downloadInputFile(request):
    expId = request.GET.get('id')
    execution = Execution.objects.get(pk=expId)

    # criar alerta
    response = HttpResponse(
        execution.inputFile, content_type='application/force-download')
    response[
        'Content-Disposition'] = 'attachment; filename="entrada-Experimento-' + str(expId) + '"'
    return response


def downloadOutputFile(request):
    expId = request.GET.get('id')
    execution = Execution.objects.get(pk=expId)
    if (execution.request_by.usuario.id == request.user.id):
        print((execution.outputFile.url))
        print("Autorizado")
        response = HttpResponse(
            execution.outputFile, content_type='application/force-download')
        response[
            'Content-Disposition'] = 'attachment; filename="Resultado-Experimento-' + str(expId) + '"'
        return response
    print("Não autorizado")
    # criar alerta
    return HttpResponseRedirect(reverse('home'))

@json_view
@csrf_protect
def checkForm(request):
    form = ExecutionForm(request.POST or None)  # request POST?

    if form.is_valid():  # processa
        experiments(request)
        helper = FormHelper()
        helper.form_id = 'form_exec'
        helper.form_action = '.'
        form_html = render_crispy_form(ExecutionForm(None), helper)
        return HttpResponseRedirect('home')

    else:
        helper = FormHelper()
        helper.form_id = 'form_exec'
        request_context = RequestContext(request)
        form_html = render_crispy_form(form, context=request_context)
        return {'success': False, 'form_html': form_html}


@csrf_protect
def fof(request):

    if request.method != 'POST':
        form = ExecutionForm(request.POST, request.FILES or None)

        if not form.is_valid():
            title = "Experiments %s" % (request.user)
            # form_html = render_crispy_form(form)
            context = {
                "form": form,
                'title': title
            }

            return render(request, "experiments.html", context)

        algorithm = request.POST.get('Algorithm')
        d_User = User.objects.get(username=request.user)
        alg = Algorithms.objects.get(nameAlg=algorithm)
        execution = Execution(
            request_by=d_User.usuariofriends,
            algorithm=alg,
        )

        execution.rperc = request.POST["Rperc"]
        execution.save()

        if (request.FILES):
            # print(request.FILES)
            fileIn = request.FILES["Input"]
            execution.inputFile = fileIn
            execution.save()
            queryInputFile = (
                settings.MEDIA_ROOT +
                execution.inputFile.name.replace('./', '/')
            ).replace(' ', '\ ')
            queryOutputFile = queryInputFile
            queryOutputFile = queryOutputFile.replace('input', 'output')
            query = alg.command + ' ' + queryInputFile + ' ' + execution.rperc + ' > ' + queryOutputFile

        else:
            query = execution.algorithm.command

        outputFilePath = './users/user_' + \
            str(execution.request_by.usuario.id) + \
            '/' + str(execution.id) + '/output'

        teste = RunExperiment.delay(query, execution.id)
        execution.save()
        title = "Experiments %s" % (request.user)

        return HttpResponseRedirect(reverse('home'))

    form = ExecutionForm(request.POST or None)
    title = "Experiments %s" % (request.user)
    context = {
        "title": title,
        "form": form
    }

    return render(request, "experiments.html", context)

def experimentsRemove(request):

    if request.method == 'POST':
        data = request.POST.get('data')

        if data:
            ids = data.split(",")
            Execution.objects.filter(id__in=ids).delete()

    return HttpResponseRedirect(reverse('home'))


@csrf_exempt
def result(request):

    if request.method == 'POST':

        if (request.FILES):
            idExec = request.POST.get("id")
            tempo = request.POST.get("time")
            execution = Execution.objects.get(id=idExec)
            fileIn = request.FILES["file"]
            execution.outputFile = fileIn
            execution.status = 3
            execution.time = tempo
            execution.save()

    return HttpResponse(1)
