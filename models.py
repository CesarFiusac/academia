from django.db import models

# Create your models here.

class Nuevoalumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    DPI = models.CharField(max_length=50)
    fechanacimiento = models.DateField()
    tel = models.CharField(max_length=50)
    nombreusuario = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    contraseniaconfirm = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} ({self.apellido})'


class Catedratico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    DPI = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
    contraseniaconfirm = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre} ({self.apellido})'
    

class Curso(models.Model):
    nombrecurso = models.CharField(max_length=60, default='Matematica Intermedia 3')
    codigo = models.CharField(max_length= 5)
    costo = models.CharField(max_length=10)
    horario = models.CharField(max_length=60)
    cupo = models.IntegerField() 
    catedratico = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombrecurso} {self.codigo} ({self.cupo})'