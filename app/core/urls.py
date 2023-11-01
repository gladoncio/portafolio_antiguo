import imp
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .forms import MyAuthForm

urlpatterns = [
    path('',views.index, name='index'),
    path('idioma<int:id>',views.idioma, name='idioma'),
]