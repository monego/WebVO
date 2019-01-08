from django.urls import path
from fof.views import fof, about

app_name = 'fofapp'
urlpatterns = [
    path('experiments', fof, name="fof"),
    path('about', about, name="about"),
]
