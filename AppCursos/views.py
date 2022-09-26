import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCursos.models import Usuario,Curso
from AppCursos.forms import Form_Usuario, UserRegisterForm

from django.views.generic import ListView#ver
from django.views.generic.detail import DetailView#ver
from django.views.generic.edit import CreateView, UpdateView, DeleteView#ver

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def inicio(request):
    return render(request, "inicio.html")

def cursos(request):
    return render(request, "cursos.html")

def usuarios(request):
    if request.method == "POST":
       usuario =  Usuario(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
       usuario.save()
       return render(request, "inicio.html")
    return render(request, "usuarios.html")

def api_usuarios(request):
    if request.method == "POST":
        formulario = Form_Usuario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = Usuario( nombre = informacion['nombre'],apellido = informacion['apellido'], email = informacion['email'])
            usuario.save()
            return render(request, "api_usuario.html")
    else:
        formulario = Form_Usuario()
    return render(request, "api_usuario.html", {"formulario": formulario})

def buscar_usuario(request):
    if request.GET["email"]:
        email = request.GET["email"]
        usuario = Usuario.objects.filter(email__icontains = email) 
        return render(request, "usuario.html", {"usuario": usuario})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def create_usuario(request):
    if request.method == 'POST':
        usuario = Usuario(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        usuario.save()
        usuarios = Usuario.objects.all()    
        return render(request, "usuarioCRUD/read_usuario.html", {"usuario": usuarios})
    return render(request, "usuarioCRUD/create_usuario.html")

def read_usuario(request=None):
    usuarios = Usuario.objects.all() #Trae todo
    return render(request, "usuraioCRUD/read_usuarios.html", {"usuario": usuarios})

def update_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id = usuario_id)

    if request.method == 'POST':
        formulario = Form_Usuario(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.nombre = informacion['nombre']
            usuario.apellido = informacion['apellido']
            usuario.email = informacion['email']
            usuario.save()
            usuarios = Usuario.objects.all() #Trae todo
            return render(request, "usuarioCRUD/read_usuario.html", {"usuario": usuario})
    else:
        formulario = Form_Usuario(initial={'nombre':usuario.nombre, 'apellido': usuario.apellido, 'email': usuario.email})
    return render(request,"estudiantesCRUD/update_usuario.html", {"formulario": formulario})

def delete_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id =  usuario_id)
    usuario.delete()

    usuarios = Usuario.objects.all()    
    return render(request, "usuarioCRUD/read_usuario.html", {"usuario": usuarios})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login(request, user)
                return render(request, "home.html")
            else:
                return render(request, "login.html", {'form':form})
        else:
            return render(request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
       
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/AppCursos/login")
    
    else:
        form = UserRegisterForm()
        return render(request, "registro.html", {'form': form})
        

    