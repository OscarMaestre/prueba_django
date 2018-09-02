from django.shortcuts import render,redirect
from django.forms import ModelForm
from reparto.models import Reparto, Profesor, Modulo, Asignacion

# Create your views here.

class RepartoForm(ModelForm):
    class Meta:
        model=Reparto
        fields= ['nombre']

class AsignacionForm(ModelForm):
    class Meta:
        model=Asignacion
        fields= ['profesor', 'modulo']
            
def crear_reparto(peticion):
    if peticion.method=="POST":
        print("Has enviado datos")
        
        formulario=RepartoForm(peticion.POST)
        formulario.save()
        nombre_del_reparto=formulario.cleaned_data["nombre"]
        return redirect('repartir', nombre_reparto=nombre_del_reparto)
    else:
        formulario_creacion_reparto=RepartoForm()
        
        diccionario_para_plantilla=dict()
        diccionario_para_plantilla["formulario"]=formulario_creacion_reparto.as_table()
        return render (peticion, "reparto/crear_reparto.html", diccionario_para_plantilla)
        
        
def obtener_modulos_sin_asignar_en_este_reparto(nombre_reparto):
    modulos_sin_asignar=[]
    asignacion=Asignacion.objects.filter()
    
def repartir(peticion, nombre_reparto):
    if peticion.method=="POST":
        asignacion=AsignacionForm(peticion.POST)
        objeto_reparto=Reparto.objects.get(nombre=nombre_reparto)
        asignacion.reparto_id=objeto_reparto.id
        asignacion.save()
        
        return redirect('repartir', nombre_reparto=nombre_del_reparto)
    else:
        diccionario=dict()
        diccionario["nombre_reparto"]=nombre_reparto
        profesores=Profesor.objects.all()
        diccionario["profesores"]=profesores
        asignacion=AsignacionForm()
        diccionario["asignacion"]=asignacion
        return render(peticion, "reparto/repartir.html", diccionario)
    
    
    
    
    
    