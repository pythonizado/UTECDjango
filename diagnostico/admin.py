#admin.py
from django.contrib import admin
from .models import *



admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Pregunta)
admin.site.register(Respuesta)

