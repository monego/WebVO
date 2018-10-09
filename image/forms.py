from django import forms

# maximum size 25MB input file
def file_size(value):
    limit = 26214400
    if value.size > limit:
        raise ValidationError(('Arquivo muito grande. '
                              'Tamanho máximo deve ser de 20MB.'))
        return render(request, "image.html")


class ImageForm(forms.Form):
    Algorithm = forms.ChoiceField(
        label="Algoritmo", required=True,
        choices=(("regularization", "Regularização"), ("wavelet", "Wavelet")))
    Input = forms.FileField(label="Imagem", required=True, validators=[file_size])
    Wavelet = forms.ChoiceField(label="Wavelet", choices=(("db1", "db1"), ("db2", "db2"), ("db3", "db3")))
    Method = forms.ChoiceField(label="Método", choices=(("visushrink", "VisuShrink"), ("bayeshrink", "BayesShrink")))
