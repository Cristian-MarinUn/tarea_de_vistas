# app_usuario/views.py
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

class RegistroUsuarioView(View):
    def get(self, request):
        return render(request, "app_usuario/registro.html")

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmar = request.POST.get("confirmar")

        # Validaciones simples
        if password != confirmar:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, "app_usuario/registro.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Este correo ya está registrado.")
            return render(request, "app_usuario/registro.html")

        # Crear usuario
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect("registro_exitoso")
