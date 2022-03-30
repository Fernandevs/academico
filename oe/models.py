from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Career(models.Model):
    CAREERS = (
        ('LC', 'Licenciatura en Contaduría'),
        ('LA', 'Licenciatura en Administración'),
        ('IBM', 'Ingeniería Biomédica'),
        ('IBQ', 'Ingeniería Bioquímica'),
        ('IEO', 'Ingeniería Electrónica'),
        ('IEA', 'Ingeniería Eléctrica'),
        ('II', 'Ingeniería Industrial'),
        ('IMOC', 'Ingeniería Mecatrónica'),
        ('IMEC', 'Ingeniería Mecánica'),
        ('IGE', 'Ingeniería en Gestión Empresarial'),
        ('IM', 'Ingeniería en Materiales'),
        ('ISC', 'Ingeniería en Sistemas Computacionales'),
        ('ITIC', 'Ingeniería en Tecnologías de la Información y Comunicaciones'),
        ('MIA', 'Maestría en Ingeniería Administrativa'),
        ('MSC', 'Maestría en Sistemas Computacionales'),
        ('MCI', 'Maestría en Ciencias en Ingeniería Electrónica'),
        ('MCIE', 'Maestría en Ciencias en Ingeniería Eléctrica'),
        ('MC', 'Maestría en Ciencias en Metalurgia'),
        ('DCI', 'Doctorado en Ciencias de la Ingeniería'),
        ('DC', 'Doctorado en Ciencias en Ingeniería Eléctrica')
    )
    career = models.CharField(max_length=20, choices=CAREERS)


class Student(models.Model):
    plan = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    year = models.DateField()
    no_de_ficha = models.PositiveIntegerField()
    no_de_control = models.CharField(max_length=8)
    escuela_de_procedencia = models.CharField(max_length=255)
    promedio = models.DecimalField(max_digits=3, decimal_places=2)
    localidad_de_origen = models.CharField(max_length=255)
    municipio_de_origen = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1)
    edad = models.PositiveSmallIntegerField()
    calificacion_del_examen_de_ingreso = models.DecimalField(max_digits=3, decimal_places=2)


"""class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']"""
