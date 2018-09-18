from django.urls import path
from . import views

urlpatterns = [
    path('experiments/checkForm',
         views.checkForm,
         name="checkForm"),
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
