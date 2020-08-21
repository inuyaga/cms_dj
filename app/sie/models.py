from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator,MaxLengthValidator


# Create your models here.
class Empresa(models.Model):
    empresa_id = models.AutoField(primary_key= True)
    empresa_nombre = models.CharField(max_length=50, verbose_name="Nombre de la empresa")
    empresa_RFC =  models.CharField(validators=[MinLengthValidator(13)], max_length=13, verbose_name="RFC de la empresa")
    empresa_Direccion= models.CharField(max_length=100, verbose_name="Dirección fiscal de la empresa")
    def __str__(self):
        return self.empresa_nombre

class Nivel(models.Model):
    nivel_id = models.AutoField(primary_key= True)
    nivel_nombre=models.CharField(max_length=30, verbose_name="Nombre del nivel")
    nivel_fechaC = models.DateTimeField(auto_now_add=True)
    nivel_idEmpresa = models.ForeignKey(Empresa, verbose_name="Id empresa", on_delete=models.CASCADE)
    def __str__(self):
        return self.nivel_nombre

class Grado(models.Model):
    grado_id= models.AutoField(primary_key=True)
    grado_nombre =  models.CharField(max_length=30, verbose_name="Nombre del grado")
    grado_fechaC = models.DateTimeField(auto_now_add=True)
    grado_idNivel = models.ForeignKey(Nivel, verbose_name="Id del nivel", on_delete=models.CASCADE)
    def __str__(self):
        return self.grado_nombre

class Prospecto(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_padre = models.CharField(max_length=50, verbose_name="Nombre completo del tutor")
    p_padre2 = models.CharField(blank=True, null=True, max_length=50, verbose_name="Nombre del segundo tutor")
    p_correo = models.EmailField(verbose_name="Correo electrónico")
    p_telefono = models.CharField(max_length=12, verbose_name="Número de teléfono")
    p_provieneEscuela = models.CharField(max_length=50, verbose_name="Escuela de proveniencia")
    p_grado = models.ForeignKey(Grado, verbose_name="Id del grado", on_delete=models.CASCADE)
    p_alumno = models.CharField(max_length=50, verbose_name="Nombre del alumno")
    p_alumno2 = models.CharField(blank=True, null=True, max_length=50, verbose_name="Nombre del segundo alumno")
    p_alumno3 = models.CharField(blank=True, null=True, max_length=50, verbose_name="Nombre del tercer alumno")
    p_fechaC = models.DateTimeField(auto_now_add=True)
    p_estatus = models.IntegerField(default=1)
    p_imagenIdentidad = models.ImageField(upload_to="admisiones", verbose_name="Identificación oficial tutor")
    def __str__(self):
        return self.p_correo