from django.contrib.auth.models import User
from django.db import models
from webfriends.models import UsuarioFriends


class Algorithms(models.Model):
    idAlg = models.AutoField(primary_key=True)
    nameAlg = models.CharField(null=False, blank=False, max_length=100)
    desc = models.CharField(null=True, blank=False, max_length=500)
    command = models.CharField(null=False, blank=False, max_length=100)

    class Meta:
        managed = True
        db_table = 'algoritmo'

    def __unicode__(self):
        return self.nameAlg


def user_directory_path_in(instance, filename):
    return './users/user_{0}/{1}/input'.format(
        instance.request_by.usuario.id, instance.id)


def user_directory_path_out(instance, filename):
    return './users/user_{0}/{1}/output'.format(
        instance.request_by.usuario.id, instance.id)


class FoF(models.Model):
    request_by = models.ForeignKey(UsuarioFriends, models.PROTECT)
    date_requisition = models.DateTimeField(
        'date_requisition',
        auto_now_add=True)
    status = models.IntegerField(default=1)
    algorithm = models.ForeignKey(Algorithms,
                                  models.PROTECT)
                              #    null=True,
                              #    blank=False)
    inputFile = models.FileField(upload_to=user_directory_path_in, null=True)
    rperc = models.FloatField()
    outputFile = models.FileField(upload_to=user_directory_path_out, null=True)
    time = models.FloatField(default=-1)

    class Meta:
        managed = True
        db_table = 'execucao'
