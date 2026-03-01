#models.py
from django.db import models
from django.contrib.auth.models import User

class Bloque(models.TextChoices):  
    ALGEBRA = 'Algebra', 'Algebra'
    MODELIZACION = 'Modelizacion', 'Modelizacion'
    FUNCIONES_GRAFICAS = 'Funciones_Graficas', 'Funciones_Graficas'
    LOGICA = 'Logica', 'Logica'

class Seleccion(models.TextChoices):
    A = 'A', 'A'
    B = 'B', 'B'
    C = 'C', 'C'
    D = 'D', 'D'
    
class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, null=True)
       
    def __str__(self): 
        return self.nombre

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    documento = models.CharField(max_length=20, null=True)
    nombre = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100, null=True)
    celular = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=254, null=True)
    password = models.CharField(max_length=150, null=True)
    tipo_usuario = models.CharField(max_length=10, default='profesor') 

    def save(self, *args, **kwargs):
        # Crear un usuario si no existe
        if not self.user:
            user = User.objects.create_user(
                username=self.documento,
                password=self.documento  # Password igual al documento
            )
            self.user = user
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    documento = models.CharField(max_length=20, null=False)
    nombre = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100, null=True)
    celular = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=254, null=True)
    password = models.CharField(max_length=150, null=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, null=True)
    tipo_usuario = models.CharField(max_length=10, default='estudiante')

    def save(self, *args, **kwargs):
        # Crear un usuario si no existe
        if not self.user:
            user = User.objects.create_user(
                username=self.documento,
                password=self.documento  # Password igual al documento
            )
            self.user = user
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    block = models.CharField(max_length=20, choices=Bloque.choices, null=True)
    descripcion = models.CharField(max_length=150, null=True)
    numero = models.DecimalField(max_digits=3, decimal_places=0, null=True)
    respuestaOK = models.CharField(max_length=1)

    def __str__(self):
        return f"Pregunta {self.descripcion} - {self.numero} - ${self.block}"

class Respuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    seleccion = models.CharField(max_length=1, choices=Seleccion.choices, blank=True, null=True)
    preguntaFK = models.ForeignKey(Pregunta, on_delete=models.SET_NULL, null=True)
    estudianteFK = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"Descuento {self.estudianteFK} - {self.seleccion}"  

