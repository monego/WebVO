from django.contrib.auth.models import User
from django.shortcuts import render
from image.forms import ImageForm
from image.tasks import ImageExperiment
from resulttable.models import Execution

def image(request):

    if request.method == 'POST':

        form = ImageForm(request.POST, request.FILES or None)

        if not form.is_valid():
            title = "Experiments %s" % (request.user)

            context = {
                "form": form,
                "title": title
            }

            return render(request, "image.html", context)

        algorithm = request.POST['Algorithm']
        d_User = User.objects.get(username=request.user)
        inputFile = request.FILES["Input"]
        wavelet = request.POST.get("Wavelet")
        method = request.POST.get("Method")
        execution = Execution(
            request_by=d_User.usuariofriends,
            inputFile = request.FILES["Input"],
        )

        execution.save()

        ImageExperiment.delay(('wavelet', inputFile, wavelet, method))

        return HttpResponseRedirect(reverse('home'))

    form = ImageForm(request.POST or None)

    title = "Experiments %s" % (request.user)
    context = {
        "title": title,
        "form": form
    }

    return render(request, "image.html", context)
