from django.shortcuts import render
from image.forms import ImageForm
from image.tasks import ImageExperiment
from resulttable.models import Execution

def image(request):
    form = ImageForm(request.POST or None)

    if form.is_valid():
        algorithm = request.POST.get('ImageAlgorithm')
        d_User = User.objects.get(username=request.user)
        alg = ImageAlgorithm.objects.get(nameAlg=algorithm)
        inputFile = request.FILES["Input"]
        wavelet = request.POST.get("wavelet")
        method = request.POST.get("method")
        execution = Execution(
            request_by=d_User.usuariofriends,
            image_algorithm=alg,
            inputFile = request.FILES["Input"],
            wavelet=wavelet,
            method=method
        )

        execution.save()

        ImageExperiment.delay((alg, inputFile, wavelet, method))

        return HttpResponseRedirect(reverse('home'))

    title = "Experiments %s" % (request.user)

    context = {
        "form": form,
        "title": title
    }

    return render(request, "image.html", context)
