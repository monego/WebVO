from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.home,
         name="home"),
    path('experiments/checkForm',
         views.checkForm,
         name="checkForm"),
    path('experiments/',
         views.home,
         name='exp'),
    path('experiments/fof',
         views.fof,
         name="fof"),
    path('experiments/remove',
         views.experimentsRemove,
         name='expRemove'),
    path('experiments/downloadInputFile',
         views.downloadInputFile,
         name='downloadInputFile'),
    path('experiments/downloadOutputFile',
         views.downloadOutputFile,
         name='downloadOutputFile'),
    path('experiments/result',
         views.result,
         name='result'),
    ]
