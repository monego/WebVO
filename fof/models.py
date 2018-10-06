from django.contrib.auth.models import User
from django.db import models
from webfriends.models import UsuarioFriends


class FoFAlgorithm(models.Model):
    idAlg = models.AutoField(primary_key=True)
    nameAlg = models.CharField(null=False, blank=False, max_length=100)
    desc = models.CharField(null=True, blank=False, max_length=500)
    command = models.CharField(null=False, blank=False, max_length=100)

    class Meta:
        managed = True
        db_table = 'fof_algorithm'

    def __unicode__(self):
        return self.nameAlg
