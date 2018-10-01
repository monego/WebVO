from django.urls import path
from . import views

urlpatterns = [
    path('experiments/fof',
         views.fof,
         name="fof"),
    ]
