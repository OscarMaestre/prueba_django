from django.urls import path

from . import views

urlpatterns = [
    path('crear_reparto', views.crear_reparto, name='crear_reparto'),
]