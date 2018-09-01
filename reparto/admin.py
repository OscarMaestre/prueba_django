from django.contrib import admin
from .models import Asignacion, Modulo, Profesor, Reparto
# Register your models here.

admin.site.register(Modulo)
admin.site.register(Asignacion)
admin.site.register(Profesor)
admin.site.register(Reparto)
