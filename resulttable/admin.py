from django.contrib import admin
from resulttable.models import Execution


class ExecutionAdmin(admin.ModelAdmin):
        fields = ['status', 'request_by', 'algorithm']
        list_display = ['request_by',
                        'time',
                        'date_requisition',
                        'status',
                        'inputFile',
                        'outputFile']


admin.site.register(Execution, ExecutionAdmin)
