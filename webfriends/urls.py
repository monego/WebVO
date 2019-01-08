from . import regbackend
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
import fof
import image
import resulttable

urlpatterns = [
    path('', include('image.urls')),
    path('', include('resulttable.urls')),
    path('experiments/', views.table, name="experiments"),

    path('fof/', include('fof.urls', namespace='fofapp')),
    path('admin/', admin.site.urls),

    path('accounts/register/', regbackend.MyRegistrationView.as_view(),
         name='register_custom'),
    path('accounts/', include('registration.backends.default.urls')),

    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('', views.home, name="home"),

    path('register/complete/',
         TemplateView.as_view(template_name='registration/registration_complete.html'),
         name='registration_complete'),
    path('register/closed/',
         TemplateView.as_view(template_name='registration/registration_closed.html'),
         name='registration_disallowed'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
