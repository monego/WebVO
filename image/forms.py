from django import forms
from django.utils.safestring import mark_safe

# maximum size 25MB input file
def file_size(value):
    limit = 26214400
    if value.size > limit:
        raise ValidationError(('Arquivo muito grande. '
                              'Tamanho máximo deve ser de 20MB.'))
        return render(request, "image.html")


class WaveletForm(forms.Form):
    Input = forms.ImageField(label="Image", required=True, validators=[file_size])
    Wavelet = forms.ChoiceField(label=mark_safe("<a href='http://scikit-image.org/docs/dev/api/skimage.restoration.html#denoise-wavelet'>Wavelet</a>"), choices=(("db1", "db1"), ("db2", "db2"), ("db3", "db3")))
    Method = forms.ChoiceField(label=mark_safe("<a href='http://scikit-image.org/docs/dev/api/skimage.restoration.html#denoise-wavelet'>Method</a>"), choices=(("visushrink", "VisuShrink"), ("bayeshrink", "BayesShrink")))
    ShiftAmount = forms.IntegerField(label=mark_safe("<a href='http://scikit-image.org/docs/dev/auto_examples/filters/plot_cycle_spinning.html'>Shift amount</a>"), min_value=0, max_value=100)
    Format = forms.ChoiceField(label="Format", choices=(("bmp", "BMP"), ("png", "PNG")))
