from django.contrib import admin
from image.models import ImageAlgorithm


class AlgAdmin(admin.ModelAdmin):
        fields = ['nameAlg', 'desc']
        list_display = ['idAlg',
                        'nameAlg',
                        'desc']


admin.site.register(ImageAlgorithm, AlgAdmin)
