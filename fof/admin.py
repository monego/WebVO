from django.contrib import admin
from .models import FoFAlgorithm


class AlgAdmin(admin.ModelAdmin):
        fields = ['nameAlg', 'desc', 'command']
        list_display = ['idAlg',
                        'nameAlg',
                        'desc']


# class NotesAdmin(admin.ModelAdmin):
# 	fields = ['user', 'execution']
# 	list_display = ['id','user',' executions']

admin.site.register(FoFAlgorithm, AlgAdmin)
