from django.forms import model_to_dict
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .models import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def inicio(request):
    publicaciones = Publicaciones.objects.all()
    ultimas = publicaciones[len(publicaciones)-4:len(publicaciones)-1]
    ultima_publicacion = publicaciones[publicaciones.count()-1]
    total_publicaciones = publicaciones.count()
    imagenes = Publicaciones.objects.filter(imagen_info__enabled=True)

    usuarios = User.objects.all()        
    total_usuarios = usuarios.count()    

    return render(request, "PruebaFinalApp/index.html", {"publicaciones":ultimas, 'total_usuarios':total_usuarios, 'total_publicaciones':total_publicaciones, 'ultima_publicacion':ultima_publicacion, "url":imagenes[0].imagen.url})

@login_required
def publicaciones(request):
        return render(request, 'PruebaFinalApp/publicaciones.html', {})
    
    


def registro(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')            
            else:
                return redirect('login')
        
        return render(request, 'PruebaFinalApp/registro.html', {"form":form})
    
    form = UserRegisterForm()

    return render(request, 'PruebaFinalApp/registro.html', {"form":form})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"PruebaFinalApp/login.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")

@login_required
def editar_perfil(request):

    user = request.user

    if request.method == "POST":

        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            user.email = info['email']
            user.first_name = info['first_name']
            user.last_name = info['last_name']

            user.save()

            return redirect('inicio')

    else:
        form = UserEditForm(initial={'email':user.email, "first_name":user.first_name, "last_name":user.last_name})
    
    return render (request, 'PruebaFinalApp/editarPerfil.html', {"form":form})

@login_required
def perfil(request):      
    
    return render(request, "PruebaFinalApp/perfil.html",{})

def crear_publicacion(request):
    if request.method == "POST":
        publicacion = CrearPublicacion(request.POST)
        print(publicacion)

        if publicacion.is_valid():
            informacion = publicacion.cleaned_data

            publicacion_nueva = Publicaciones(pais=informacion['pais'], titulo=informacion['titulo'], descripcion=informacion['descripcion'], fecha_viaje=informacion['fecha_viaje'])

            publicacion_nueva.save()

            return redirect ('inicio')

    else:

        publicacion = CrearPublicacion()

        return render(request, 'PruebaFinalApp/crearpublicacion.html', {'publicacion':publicacion})

    

