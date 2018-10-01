from django.contrib.auth.models import User
from django.db import models


class UsuarioFriends(models.Model):
    nickname = models.CharField(
        default='default', max_length=30, blank=False, null=True)
    company = models.CharField(
        default='default', max_length=50, blank=False, null=True)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    date_register = models.DateTimeField('date_register', auto_now_add=True)
    last_access = models.DateTimeField('last_access', auto_now=True)
    resultsPerPage = models.IntegerField(default=10)

    class Meta:
        managed = True
        db_table = 'usuario'

    def __unicode__(self):
        return self.nickname
