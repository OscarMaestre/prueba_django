from django.urls import path

from . import views

urlpatterns = [
    path('crear_reparto', views.crear_reparto, name='crear_reparto'),
    path('repartir/<str:nombre_reparto>', views.repartir, name='repartir'),
    path('repartir2/<str:nombre_reparto>', views.repartir2, name='repartir2'),
    path('borrar/<int:modulo_id>/<int:profesor_id>/<str:nombre_reparto>', views.borrar, name='borrar'),
]