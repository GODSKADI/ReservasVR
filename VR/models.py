from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Curso(models.Model):
	nombre = models.CharField(max_length = 200)
	clase = models.CharField(max_length = 200)

class Aula(models.Model):
	nombre = models.CharField(max_length = 200)
	num_gafas = models.IntegerField(default = 0)
	aforo = models.IntegerField(default = 0)

class Reserva(models.Model):
	nombre = models.ForeignKey(User, on_delete = models.CASCADE)
	num_personas = models.IntegerField(default = 0)
	num_gafas = models.IntegerField(default = 0)
	aula = models.ForeignKey(Aula, on_delete = models.CASCADE)
	fecha_hora = models.DateTimeField(default = timezone.now) 
	incio_hora = models.DateTimeField(default = timezone.now)
	final_hora = models.DateTimeField(default = timezone.now)

class Gafa(models.Model):
	nombre = models.CharField(max_length = 200)
	aula = models.ForeignKey(Aula, on_delete = models.CASCADE)
	