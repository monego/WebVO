from crispy_forms.helper import FormHelper
from crispy_forms.utils import render_crispy_form
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from jsonview.decorators import json_view
from .models import Execution


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
            'Content-Disposition'] = 'attachment; filename="Result-Experiment-' + str(expId) + '"'
        return response
    print("Not authorized")
    # criar alerta
    return HttpResponseRedirect(reverse('home'))

def downloadLogFile(request):
    expId = request.GET.get('id')
    log = Execution.objects.get(pk=expId)
    if (log.request_by.usuario.id == request.user.id):
        print((log.logFile))
        print("Autorizado")
        response = HttpResponse(
            log.outputFile, content_type='application/force-download')
        response[
            'Content-Disposition'] = 'attachment; filename="Logfile-Experiment-' + str(expId) + '"'
        return response
    print("Not authorized")

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

def experimentsRemove(request):

    if request.method == 'POST':
        data = request.POST.get('data')

        if data:
            ids = data.split(",")
            Execution.objects.filter(id__in=ids).delete()

    return HttpResponseRedirect(reverse('experiments'))


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
