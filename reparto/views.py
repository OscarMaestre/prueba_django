from django.shortcuts import render
from django.forms import ModelForm
from reparto.models import Reparto

# Create your views here.

class RepartoForm(ModelForm):
    class Meta:
        model=Reparto
        fields= ['nombre']
            
def crear_reparto(peticion):
    if peticion.method=="POST":
        print("Has enviado datos")
        formulario=RepartoForm(peticion.POST)
        formulario.save()
    else:
        formulario_creacion_reparto=RepartoForm()
        print(formulario_creacion_reparto)
        diccionario_para_plantilla=dict()
        diccionario_para_plantilla["formulario"]=formulario_creacion_reparto.as_table()
        return render (peticion, "reparto/crear_reparto.html", diccionario_para_plantilla)
        print ("Mostrando formulario")