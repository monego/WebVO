from django.contrib import admin
from .models import FoFAlgorithm


class ExecutionAdmin(admin.ModelAdmin):
        fields = ['status', 'request_by', 'algorithm']
        list_display = ['request_by',
                        'algorithm',
                        'time',
                        'date_requisition',
                        'status',
                        'inputFile',
                        'outputFile']


class AlgAdmin(admin.ModelAdmin):
        fields = ['nameAlg', 'desc', 'command']
        list_display = ['idAlg',
                        'nameAlg',
                        'desc']


# class NotesAdmin(admin.ModelAdmin):
# 	fields = ['user', 'execution']
# 	list_display = ['id','user',' executions']

admin.site.register(FoFAlgorithm, AlgAdmin)
