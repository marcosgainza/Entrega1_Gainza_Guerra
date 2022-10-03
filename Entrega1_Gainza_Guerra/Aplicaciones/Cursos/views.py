from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, '¡Cursos listados!')
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    puntos = request.POST['numPuntos']
    
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, puntos=puntos)
    messages.success(request, '¡Curso registrado!')
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    puntos = request.POST['numPuntos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.puntos = puntos
    curso.save()
    
    messages.success(request, '¡Curso actualizado!')

    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    
    messages.success(request, '¡Curso eliminado!')
    
    return redirect('/')