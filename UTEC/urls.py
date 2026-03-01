#urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from diagnostico import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('estudiante/', views.pagina_estudiante, name='pagina_estudiante'),
    path('profesor/', views.pagina_profesor, name='pagina_profesor'),
    path('respuestas_guardadas/', views.respuestas_guardadas, name='respuestas_guardadas'),
    path('diagnostico/', include('diagnostico.url')),
    path('registrar/estudiante/', views.registrar_estudiante, name='registrar_estudiante'),
    path('importar-estudiantes/', views.importar_estudiantes, name='importar_estudiantes'),
    path('registrar/profesor/', views.registrar_profesor, name='registrar_profesor'),
    path('crear_carrera', views.crear_carrera, name='crear_carrera'),
    path('registro/exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('no-autorizado/', views.pagina_no_autorizada, name='pagina_no_autorizada'),
    path('informes', views.informes, name='informes'),
    path('informes/correctas_por_pregunta/', views.correctas_por_pregunta, name='correctas_por_pregunta'),
    path('informes/opciones_por_pregunta/', views.opciones_por_pregunta, name='opciones_por_pregunta'),
    path('informes/correctas_por_bloque/', views.correctas_por_bloque, name='correctas_por_bloque'),
    path('informes/comparacion_bloques/', views.comparacion_bloques, name='comparacion_bloques'),
    path('buscar_estudiante/', views.buscar_estudiante, name='buscar_estudiante'),
    path('todito/', views.todito, name='todito'),
    path('actualizar_respuestas/<int:estudiante_id>/', views.actualizar_respuestas, name='actualizar_respuestas'),

]