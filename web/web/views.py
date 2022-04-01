# Importamos HttpResponse que es para mostrar contenido
from django.http import HttpResponse

def saludo(request): # Primero vista ahora debemos modificar urls.py
    return HttpResponse("Hola alumnos")
