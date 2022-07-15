from django.urls import path

from .views import *

urlpatterns = [
    
    path('', inicio, name='inicio'),
    path('publicaciones', publicaciones, name='publicaciones'),
    path('registro', registro, name='registro'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('editarperfil', editar_perfil, name='editar_perfil'),  
    path('crearpublicacion', crear_publicacion, name='crear_publicacion'),
    path('mis_publicaciones', ver_publicaciones, name='ver_publicaciones'),    
]