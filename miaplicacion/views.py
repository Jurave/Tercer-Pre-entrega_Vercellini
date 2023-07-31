from django.shortcuts import render
from django.http import HttpResponse
from miaplicacion.models import *
from .forms import *




# Create your views here.
def index(request):
    return render(request, "miaplicacion/base.html")


def usuarios(request):
    ctx = {"usuarios": Usuarios.objects.all() }
    return render(request, "miaplicacion/usuarios.html", ctx)

def categorias(request):
    ctx = {"categorias": Categorias.objects.all() }
    return render(request, "miaplicacion/categorias.html", ctx)

def posteos(request):
    ctx = {"posteos": Posteos.objects.all() }
    return render(request, "miaplicacion/posteos.html", ctx)

def usuarioForm(request):
    if request.method == "POST":
        usuario = Usuarios(nombre=request.POST['nombre'], email=request.POST['email'])
        usuario.save()
        return HttpResponse ("Se grabo con éxito el usuario!")

    return render(request,'miaplicacion/usuarioForm.html')

def usuarioForm2(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            usuario = Usuarios(nombre=informacion['nombre'], email=informacion['email'])
            usuario.save()
            return render(request, "miaplicacion/base.html")
    else:        
         miForm = UsuarioForm()
    return render(request, "miaplicacion/usuarioform2.html", {"form":miForm})
    

def categoriaForm2(request):
    if request.method == "POST":
        miForm = CategoriaForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            categoria = Categorias(nombre=informacion['nombre'], redsocial=informacion['redsocial'], autorpublica=informacion['autorpublica'])
            categoria.save()
            return render(request, "miaplicacion/base.html")
    else:        
         miForm = CategoriaForm()
    return render(request, "miaplicacion/categoriaForm2.html", {"form":miForm})


def posteosForm2(request):
    if request.method == "POST":
        miForm = PosteosForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            posteo = Posteos(nombre=informacion['nombre'], categoria=informacion['categoria'], redsocial=informacion['redsocial'])
            posteo.save()
            return render(request, "miaplicacion/base.html")
    else:        
         miForm = PosteosForm()
    return render(request, "miaplicacion/posteoForm2.html", {"form":miForm})


def buscarEmail(request):
    return render(request, "miaplicacion/buscarEmail.html")


def buscar2(request):
    if request.GET['email']:
        email = request.GET['email']
        user = Usuarios.objects.filter(email__icontains=email)
        return render(request, "miaplicacion/resultadosEmail.html", {"email": email, "user": user})
    
    return HttpResponse("No se ingresaron datos para buscar!")