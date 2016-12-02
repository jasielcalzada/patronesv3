from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator,MaxValueValidator
from django.utils import timezone
import datetime
import time

# Create your models here.

class QuerySet(models.QuerySet):

	def get_categoria(self):
		return self.nombre

class Usuario(models.Model):
	ID_Usuario = models.AutoField(primary_key=True)
	user_perfil = models.OneToOneField(User, related_name="profile")
	email = models.EmailField()
	name = models.CharField(max_length=64)
	last = models.CharField(max_length=64)

	def __unicode__(self):
		return '%s'%(self.name)

	def __str__(self):
		return 'nombre: %s' %(self.name)

class Categoria(models.Model):
	ID_Categoria = models.AutoField(primary_key=True)
	num_cat = models.IntegerField(unique=True)
	nombre = models.CharField(max_length=100)

	def _unicode_(self):
		return 'Categoria %d: %s' %(self.num_cat, self.nombre)

	def __str__(self):
		return self.nombre


class Pregunta_Opcion(models.Model):
	ID_Pregunta_Opcion = models.AutoField(primary_key=True)
	pregunta = models.CharField(max_length=100)
	categoria = models.ForeignKey(Categoria)
	fecha_creacion = models.DateField(default=datetime.date.today)
	publicado = models.BooleanField(default=True)
	ID_Usuario = models.ForeignKey(Usuario)

	class Meta:
		ordering = ['-fecha_creacion']


	"""def cuenta_elecciones(self):
		return self.set_eleccion.count()

	def cuenta_votos_totales(self):
		resultado = 0
		for eleccion in self.set_eleccion.all():
			resultado += eleccion.contar_votos()
		return resultado

	def puede_votar(self,Usuario):
		return not self.set_voto.filter(user=Usuario).exists()"""

	def __unicode__(self):
		return '%s'%(self.ID_Pregunta_Opcion)

	def __str__(self):
		return self.pregunta

class Opcion_Pregunta(models.Model):
	ID_Opcion_Pregunta = models.AutoField(primary_key=True)
	opcion = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200, blank=True, null=True)
	ID_Pregunta_Opcion = models.ForeignKey(Pregunta_Opcion)

	def __str__(self):
		return self.opcion

class Pregunta_Abierta(models.Model):
	ID_Pregunta_Abierta = models.AutoField(primary_key=True)
	pregunta = models.CharField(max_length=100)
	categoria = models.ForeignKey(Categoria)
	fecha_creacion = models.DateField(default=datetime.date.today)
	publicado = models.BooleanField(default=True)
	ID_Usuario = models.ForeignKey(Usuario)

	def __str__(self):
		return self.pregunta

"""class Pregunta(models.Model):
	ID_Pregunta = models.AutoField(primary_key=True)
	ID_Pregunta_Opcion = models.ForeignKey(Pregunta_Opcion)
	ID_Pregunta_Abierta = models.ForeignKey(Pregunta_Abierta)"""

class Respuesta(models.Model):
	ID_Respuesta = models.AutoField(primary_key=True)
	respuesta = models.CharField(max_length=200)
	ID_Usuario = models.ForeignKey(Usuario)
	ID_Pregunta_Abierta = models.ForeignKey(Pregunta_Abierta)

	"""def contar_votos(self):
		return self.set_voto.count()"""

	def __unicode__(self):
		return self.respuesta

	def __str__(self):
		return self.respuesta

class Respuesta_Opcion(models.Model):
	ID_Respuesta_Opcion = models.AutoField(primary_key=True)
	ID_Pregunta_Opcion = models.ForeignKey(Pregunta_Opcion)
	ID_Opcion_Pregunta = models.ForeignKey(Opcion_Pregunta)

	def __unicode__(self):
		return u'Voto para %s' % (self.respuesta)

	def __str__(self):
		return self.ID_Respuesta_Opcion

	"""class Meta:
		unique_together = ('Usuario', 'Pregunta')"""
