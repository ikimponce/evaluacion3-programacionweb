from django.shortcuts import render
from django.http import HttpResponse
from vacunatorio.models import Persona

def index(request):
    return render(request,"index.html")

def list(request):
    return render(request,"list.html")

def listaction(request):
    datos = Persona.objects.all()
    return render(request,'list.html',{'personas':datos})

def search(request):
    return render(request,'search.html')

def searchresult(request):
    if request.GET["txt_rut"]:
        personab = request.GET["txt_rut"]
        personas = Persona.objects.filter(rut__icontains=personab)
        return render(request,"searchresult.html",{"personas":personas,"query":personab})
    else:
        mensaje = "Debe ingresar un rut"
        return HttpResponse(mensaje+"<br><a href=''>Volver al inicio</a>")

def add(request):
    return render(request,"add.html")

def addaction(request):
    rut=request.GET["txt_rut"]
    nombre=request.GET["txt_nombre"]
    apepat=request.GET["txt_apepat"]
    apemat=request.GET["txt_apemat"]
    edad=request.GET["txt_edad"]
    nombre_vacuna=request.GET["txt_nombre_vacuna"]
    fecha=request.GET["txt_fecha"]
    if len(rut)==10 and len(nombre)>0 and len(apepat)>0 and len(apemat)>0 and len(edad)>0 and len(nombre_vacuna)>0 and len(fecha)>0:
        registro = Persona(rut=rut,nombre=nombre,apepat=apepat,apemat=apemat,edad=edad,nombre_vacuna=nombre_vacuna,fecha=fecha)
        registro.save()
        mensaje = "Persona Registrada"
    else:
        mensaje = "Debe ingresar todos los datos de la Persona"
    return HttpResponse(mensaje+"<br><a href='/index/'>Volver al inicio</a>")

