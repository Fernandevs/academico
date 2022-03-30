from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import models

from oe.models import Career, Student


class UserForm(UserCreationForm):
    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo'
        }


class CareerForm(models.ModelForm):
    class Meta:
        model = Career

        fields = [
            'career',
            'is_active'
        ]

        labels = {
            'career': 'Carrera',
            'is_active': 'Está activa'
        }


class StudentForm(models.ModelForm):
    class Meta:
        model = Student

        fields = [
            'career',
            'plan',
            'period',
            'year',
            'no_de_ficha',
            'no_de_control',
            'escuela_de_procedencia',
            'promedio',
            'localidad_de_origen',
            'municipio_de_origen',
            'sexo',
            'edad',
            'calificacion_del_examen_de_ingreso'
        ]

        labels = {
            'career': 'Carrera',
            'plan': 'Plan de estudios',
            'period': 'Periodo',
            'year': 'Año',
            'no_de_ficha': 'Número de ficha',
            'no_de_control': 'Número de control',
            'escuela_de_procedencia': 'Escuela de procedencia',
            'promedio': 'Promedio',
            'localidad_de_origen': 'Localidad de origen',
            'municipio_de_origen': 'Municipio de origen',
            'sexo': 'Sexo',
            'edad': 'Edad',
            'calificacion_del_examen_de_ingreso': 'Calificación del examen de ingreso'
        }
