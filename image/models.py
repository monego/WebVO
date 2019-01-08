from django.db import models
from webfriends.models import UsuarioFriends

class ImageAlgorithm(models.Model):
    idAlg = models.AutoField(primary_key=True)
    nameAlg = models.CharField(null=False, blank=False, max_length=100)
    desc = models.CharField(null=True, blank=False, max_length=500)

    class Meta:
        managed = True
        db_table = 'image_algorithm'

    def __str__(self):
        return self.nameAlg
