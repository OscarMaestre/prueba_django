# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.forms import ModelForm
from reparto.models import Reparto, Profesor, Modulo, Asignacion

# Create your views here.


class ProfesorEnReparto(object):
    def __init__(self, nombre, id):
        self.modulos=[]
        self.horas=0
        self.nombre=nombre
        self.id=id
    def anadir_modulo(self, modulo):
        self.modulos.append(modulo)
        self.horas=self.horas + modulo.horas
        #print("Anadiendo "+modulo.nombre+" a " + self.nombre)
    

class ListaProfesores(object):
    def __init__(self):
        self.lista_profesores=[]
    
    def anadir_profesor(self, profesor):
        objeto_profesor=ProfesorEnReparto(profesor.nombre, profesor.id)
        #print("Anadido "+profesor.nombre)
        self.lista_profesores.append(objeto_profesor)
        
    def asignar_modulo_profesor(self, profesor, modulo):
        for p in self.lista_profesores:
            if p.nombre==profesor.nombre:
                #print("Anadido para "+p.nombre)
                p.anadir_modulo(modulo)

class RepartoForm(ModelForm):
    class Meta:
        model=Reparto
        fields= ['nombre']

class AsignacionForm(ModelForm):
    class Meta:
        model=Asignacion
        fields= ['profesor', 'modulo', 'reparto']
            
def crear_reparto(peticion):
    if peticion.method=="POST":
        #print("Has enviado datos")
        
        formulario=RepartoForm(peticion.POST)
        formulario.save()
        nombre_del_reparto=formulario.cleaned_data["nombre"]
        return redirect('repartir2', nombre_reparto=nombre_del_reparto)
    else:
        formulario_creacion_reparto=RepartoForm()
        
        diccionario_para_plantilla=dict()
        diccionario_para_plantilla["formulario"]=formulario_creacion_reparto.as_table()
        return render (peticion, "reparto/crear_reparto.html", diccionario_para_plantilla)
        
        
def obtener_modulos_sin_asignar_en_este_reparto(nombre_reparto):
    reparto=Reparto.objects.get(nombre=nombre_reparto)
    #print(reparto)
    modulos_ya_asignados=reparto.asignacion_set.all().values("modulo")
    modulos_sin_asignar=Modulo.objects.all()
    # print("Conjunto global")
    # print(modulos_sin_asignar)
    # print("Ya asignados")
    # print(modulos_ya_asignados)
    diferencia=modulos_sin_asignar.exclude(pk__in=modulos_ya_asignados)
    #print(diferencia)
    
    return diferencia


def get_datos_profesores(nombre_reparto):
    objeto_reparto=Reparto.objects.get(nombre=nombre_reparto)
    asignaciones=objeto_reparto.asignacion_set
    profesores=Profesor.objects.all()
    lista_profesores=ListaProfesores()
    for p in profesores:
        lista_profesores.anadir_profesor(p)
    #print(asignaciones.all())
    for a in asignaciones.all():
        #print(a)
        modulo=a.modulo
        profesor=a.profesor
        lista_profesores.asignar_modulo_profesor(profesor, modulo)
        
    return lista_profesores.lista_profesores
    
def repartir(peticion, nombre_reparto):
    if peticion.method=="POST":
        asignacion=AsignacionForm(peticion.POST)
        asignacion.save()
        
        return redirect('repartir', nombre_reparto=nombre_reparto)
    else:
        diccionario=dict()
        diccionario["nombre_reparto"]=nombre_reparto
        profesores=Profesor.objects.all()
        diccionario["profesores"]=profesores
        objeto_reparto=Reparto.objects.get(nombre=nombre_reparto)
        modulos_no_asignados=obtener_modulos_sin_asignar_en_este_reparto(nombre_reparto)
        #print("Modulos no asignados")
        #print(modulos_no_asignados)
        asignacion=AsignacionForm(
            initial={'reparto':objeto_reparto},
            
        )
        asignacion.fields["modulo"].queryset=modulos_no_asignados;
        diccionario["asignacion"]=asignacion
        diccionario["informacion_profesores"]=get_datos_profesores(nombre_reparto)
        return render(peticion, "reparto/repartir.html", diccionario)
    
    
    
    
    
def borrar(peticion, modulo_id, profesor_id, nombre_reparto):
    reparto=Reparto.objects.get(nombre=nombre_reparto)
    reparto_id=reparto.id
    asignacion=Asignacion.objects.filter(modulo_id=modulo_id, profesor_id=profesor_id, reparto_id=reparto_id)
    print("Borrando")
    print(asignacion)
    asignacion.delete()
    return redirect('repartir2', nombre_reparto=nombre_reparto)


def index(peticion):
    repartos=Reparto.objects.all()
    diccionario=dict()
    diccionario["repartos"]=repartos
    return render(peticion, "reparto/index.html", diccionario)



def extraer_modulo_por_turno(modulos, nombre_turno):
    lista=[]
    for m in modulos:
        if m.turno==nombre_turno:
            lista.append(m)
    print()
    return lista

def repartir2(peticion, nombre_reparto):
    if peticion.method=="POST":
        try:
            print(peticion.POST)
            modulo_id=peticion.POST["modulo"]
            profesor_id=peticion.POST["profesor"]
            reparto=nombre_reparto
            print(modulo_id)
            print(profesor_id)
            objeto_modulo=Modulo.objects.get(id=modulo_id)
            objeto_reparto=Reparto.objects.get(nombre=nombre_reparto)
            
            asignacion=Asignacion()
            asignacion.modulo_id=modulo_id
            asignacion.profesor_id=profesor_id
            asignacion.reparto_id=objeto_reparto.id
            asignacion.save()
        except Exception as e:
            print("Faltan datos")
            print(e)
        
        return redirect('repartir2', nombre_reparto=nombre_reparto)
    else:
        diccionario=dict()
        diccionario["nombre_reparto"]=nombre_reparto
        profesores=Profesor.objects.all()
        diccionario["profesores"]=profesores
        objeto_reparto=Reparto.objects.get(nombre=nombre_reparto)
        modulos_no_asignados=obtener_modulos_sin_asignar_en_este_reparto(nombre_reparto)
        #print("Modulos no asignados")
        #print(modulos_no_asignados)
        asignacion=AsignacionForm(
            initial={'reparto':objeto_reparto},
            
        )
        asignacion.fields["modulo"].queryset=modulos_no_asignados;
        diccionario["modulos"]=modulos_no_asignados
        
        diccionario["modulos_matinales"]=extraer_modulo_por_turno(modulos_no_asignados, "mañana")
        diccionario["modulos_tarde"]=extraer_modulo_por_turno(modulos_no_asignados, "tarde")
        diccionario["modulos_elearning"]=extraer_modulo_por_turno(modulos_no_asignados, "elearning")
        #print(diccionario["modulos_matinales"])
        diccionario["asignacion"]=asignacion
        diccionario["informacion_profesores"]=get_datos_profesores(nombre_reparto)
        return render(peticion, "reparto/repartir2.html", diccionario)
    
    