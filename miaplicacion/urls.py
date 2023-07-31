from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name="inicio"),
    
    path('posteos/', posteos, name="posteos"),
    path('categorias/', categorias, name="categorias"),
    path('usuarios/', usuarios, name="usuarios"),


    path('usuario_form/', usuarioForm, name="usuario_form"),
    path('usuarios_form2/', usuarioForm2, name="usuarios_form2"),
    path('categorias_form2/', categoriaForm2 , name="categorias_form2"),
    path('posteos_form2/', posteosForm2, name="posteos_form2"),

     path('buscar_email/', buscarEmail, name="buscar_email"),
     path('buscar2/', buscar2, name="buscar2"),

] 