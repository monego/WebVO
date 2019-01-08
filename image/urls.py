from django.urls import path
from . import views

urlpatterns = [
    path('experiments/image/wavelet',
         views.wavelet,
         name="wavelet"),
    ]
