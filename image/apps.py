# Convenções conforme https://docs.djangoproject.com/en/2.1/ref/applications/

from django.apps import AppConfig


class ImageProcessingConfig(AppConfig):
    name = 'image'
    verbose_name = 'Algoritmos de Processamento de Imagens'
