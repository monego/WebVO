from django.db import models
from fof.models import FoFAlgorithm
from image.models import ImageAlgorithm
from webfriends.models import UsuarioFriends


def user_directory_path_in(instance, filename):
    return './users/user_{0}/{1}/input'.format(
        instance.request_by.usuario.id, instance.id)


def user_directory_path_out(instance, filename):
    return './users/user_{0}/{1}/output'.format(
        instance.request_by.usuario.id, instance.id)


class Execution(models.Model):
    request_by = models.ForeignKey(UsuarioFriends, models.PROTECT)
    date_requisition = models.DateTimeField(
        'date_requisition',
        auto_now_add=True)
    status = models.IntegerField(default=1)
    #algorithm = models.ForeignKey(FoFAlgorithm, null=True, blank=False, on_delete=models.SET_NULL)
    algorithm = models.TextField(null=True, blank=True)
    inputFile = models.FileField(upload_to=user_directory_path_in, null=True)
    outputFile = models.FileField(upload_to=user_directory_path_out, null=True)
    logFile = models.FileField(upload_to=user_directory_path_out, null=True)
    time = models.FloatField(default=-1)

    class Meta:
        managed = True
        db_table = 'execution'
