from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre      =       models.CharField(max_length=30)
    prioridad   =       models.IntegerField(default=0)
    def __str__(self):
        return str(self.prioridad)+".-"+self.nombre
    class Meta:
        ordering=["prioridad"]
    
class Modulo(models.Model):
    nombre      =       models.CharField(max_length=70)
    curso       =       models.CharField(max_length=6)
    horas       =       models.IntegerField(default=0)
    turno       =       models.CharField(max_length=15)
    class Meta:
        ordering=["nombre"]
    
    def __str__(self):
        return self.nombre +" ("+self.curso +" " + self.turno +") " + str(self.horas)+"h"
    
class Reparto(models.Model):
    nombre      =       models.CharField(max_length=70)
    def __str__(self):
        return self.nombre
    
class Asignacion(models.Model):
    profesor    =       models.ForeignKey(Profesor, on_delete=models.CASCADE)
    modulo      =       models.ForeignKey(Modulo,   on_delete=models.CASCADE)
    reparto     =       models.ForeignKey(Reparto,  on_delete=models.CASCADE)
    