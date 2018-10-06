from django.urls import path
from . import views

urlpatterns = [
    path('experiments/image',
         views.image,
         name="image"),
    ]
