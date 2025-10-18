# app_usuario/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import RegistroUsuarioView

urlpatterns = [
    path("registro/", RegistroUsuarioView.as_view(), name="registro_usuario"),
    path("registro/exitoso/", TemplateView.as_view(template_name="app_usuario/registro_exitoso.html"), name="registro_exitoso"),
]
