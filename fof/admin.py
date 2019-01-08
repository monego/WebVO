from django.contrib import admin
from .models import FoFAlgorithm


class AlgAdmin(admin.ModelAdmin):
        fields = ['nameFoF', 'descFoF', 'commandFoF']
        list_display = ['idFoF',
                        'nameFoF',
                        'descFoF']


# class NotesAdmin(admin.ModelAdmin):
# 	fields = ['user', 'execution']
# 	list_display = ['id','user',' executions']

admin.site.register(FoFAlgorithm, AlgAdmin)
