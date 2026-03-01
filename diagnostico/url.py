#url.py
from django.urls import path
from . import views  # Importar las vistas de la app

urlpatterns = [
    path('registrar/estudiante/', views.registrar_estudiante, name='registrar_estudiante'),
    path('registrar/profesor/', views.registrar_profesor, name='registrar_profesor'),
    path('registro/exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('no-autorizado/', views.pagina_no_autorizada, name='pagina_no_autorizada'),
    path('registrar/profesor/', views.registrar_profesor, name='registrar_profesor'),
    path('importar-estudiantes/', views.importar_estudiantes, name='importar_estudiantes'),
]