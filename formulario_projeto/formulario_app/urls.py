from django.urls import path
from . import views

urlpatterns = [
    path('exportar/', exportar_csv, name='exportar_csv'),
]