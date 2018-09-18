from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.home,
         name="home"),
    path('experiments/',
         views.home,
         name='exp'),
    path('experiments/fof',
         views.fof,
         name="fof"),
    ]
