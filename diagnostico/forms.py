from django import forms
from .models import Carrera, Seleccion

class RegistrarEstudianteForm(forms.Form):
    documento = forms.CharField(max_length=20, label="Documento")
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    celular = forms.CharField(max_length=15, label="Celular", required=False)
    email = forms.EmailField(label="Email", required=False)
    carrera = forms.ModelChoiceField(queryset=Carrera.objects.all(), label="Carrera")

class RegistrarProfesorForm(forms.Form):
    documento = forms.CharField(max_length=20, label="Documento")
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    celular = forms.CharField(max_length=15, label="Celular", required=False)
    email = forms.EmailField(label="Email", required=False)

class RegistrarCarreraForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    descripcion = forms.CharField(max_length=200, label="Descripcion", required=False)

class RespuestaForm(forms.Form):
    seleccion = forms.MultipleChoiceField(
        choices=Seleccion.choices,
        widget=forms.CheckboxSelectMultiple,   
        required=False
    )

class DocumentoEstudianteForm(forms.Form):
    documento = forms.CharField(
        label="Documento del estudiante",
        max_length=20,
        required=True
    )