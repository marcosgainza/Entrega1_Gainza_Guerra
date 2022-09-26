from re import template
from django.urls import path
from AppCursos.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('api_usuarios/', api_usuarios),
    path('buscar_usuario/', buscar_usuario),
    path('create_usuario/', create_usuario),
    path('read_usaurio/', read_usuario),
    path('update_usuario/<usuario_id>', update_usuario),
    path('delete_uasuario/<usaurio_id>', delete_usuario),
    path('login/', login_request),
    path('registro/', registro),
    path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name="Logout" )
    
    ]