from django.shortcuts import render
from .models import Persona,Perro
from django.shortcuts import redirect
from django.http import HttpResponse
#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.htm')

def persona_form(request):
    return render(request,'formulario_persona.htm')

def perro_form(request):
    return render(request,'formulario_perro.htm')
    
def login(request):
    return render(request,'login.htm')
    
def listado(request):
    return render(request,'listado_perro.htm',{'perros':Perro.objects.all()})

def contrasenia(request):
    return render(request,'contraseña.htm')    

def crear(request):
    correo = request.POST.get('email','')
    run = request.POST.get('run','')
    nombreC = request.POST.get('nombreC','')
    contrasenia = request.POST.get('contrasenia','')
    fecha = request.POST.get('fecha_nacimiento','')
    telefono = request.POST.get('telefono','')
    region = request.POST.get('region','')
    comuna = request.POST.get('comuna','')
    vivienda = request.POST.get('vivienda','')
    persona = Persona(correo=correo,run=run,nombreC=nombreC,contrasenia=contrasenia,fecha=fecha, telefono=telefono,region=region,comuna=comuna,vivienda=vivienda,pregunta='')
    persona.save()
    userAuth = User.objects.create_user(run, email=correo, password=contrasenia)
    userAuth.save()
    return redirect('/login/')


def crear_perro(request):
    foto = request.FILES.get('foto',False)
    nombre = request.POST.get('nombre','')
    raza = request.POST.get('raza','')
    descripcion =request.POST.get('descripcion','')
    estado = request.POST.get('estado','')
    perro = Perro(foto=foto,nombre=nombre,raza=raza,descripcion=descripcion,estado=estado)
    perro.save()
    return redirect('/index/')

def login_iniciar(request):
    usuario = request.POST.get('rut','')
    contrasenia = request.POST.get('contrasenia','')
    user = authenticate(request,username=usuario, password=contrasenia)

    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="/index/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/login/";</script>')

@login_required(login_url='/login/')
def cerrar_session(request):
    logout(request)
    return HttpResponse('<script>alert("Cierre de sesión correcto."); window.location.href="/index/";</script>')  


def cambio_contrasenia(request):
    contrasenia = request.POST.get('contrasenia','')
    persona.contrasenia = contrasenia
    persona.save()
    return redirect('/index/')