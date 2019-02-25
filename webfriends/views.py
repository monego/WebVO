from .paginator import paginate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from resulttable.models import Execution
from webfriends.forms import ContactForm, UsuarioFriendsForm
from webfriends.models import UsuarioFriends
from webfriends import settings
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.contrib import messages

import os

def home(request):
    title = "Bem-vindo"
    context = {
        "title": title
    }
    return render(request, "welcome.html", context)

def table(request):
    title = "Welcome %s" % request.user
    executionList = Execution.objects.filter( # Corrigir a lista de execução
        request_by__usuario__id=request.user.id).order_by('-id')
    try:
        UserProf = UsuarioFriends.objects.get(usuario__id=request.user.id)
    except:
        print("Erro. Criando novo userProf")
        user = User.objects.get(id=request.user.id)
        UserProf = UsuarioFriends(usuario=user)
        UserProf.save()
        os.mkdir('./users/user_' + str(request.user.id))
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


def about(request):
    return render(request, "about.html", {})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = 'Portal Friends - Mensagem de %s ' % (
            form.cleaned_data.get("nome"))
        from_email = settings.EMAIL_HOST_USER
        #from_email = form.cleaned_data.get("email")
        to_email = settings.EMAIL_HOST_USER
        message = form.cleaned_data.get("mensagem")
        user = "\n\n\nSent by:" + form.cleaned_data.get("nome") + " - " + form.cleaned_data.get("email")
        send_mail(subject,
                  message + user,
                  from_email,
                  [to_email],
                  fail_silently=False)
        messages.success(request, 'Message sent successfully.')
        return render(request, "welcome.html", {})
    else:
        context = {
            "form": form,
        }
        return render(request, "contact.html", context)