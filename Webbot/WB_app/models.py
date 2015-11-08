# -*- encoding: utf-8 -*-
from django.db import models

class oficina(models.Model):
	#id_lugar = models.AutoField(primary_key=False)
	city = models.CharField(max_length=100)
	province = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return name
	class Meta:
		verbose_name = "oficina"
		verbose_name_plural = "oficina"

class Autor(models.Model):
	id_autor = models.AutoField(primary_key=True)
	nombre_comp_autor = models.CharField(max_length=255, unique = True)
	class Meta:
		verbose_name = "Autor"
		verbose_name_plural = "Autor"

class Publicacion(models.Model):
	id_publicacion = models.AutoField(primary_key=True)
	anio_publicacion = models.CharField(max_length=10, null=True)
	titulo_publicacion = models.CharField(max_length=200, unique = True)
	cabecera_publicacion = models.CharField(max_length=300)
	isbn = models.CharField(max_length=30, null= True)
	autores = models.ManyToManyField(Autor)
	class Meta:
		verbose_name = "Publicacion"
		verbose_name_plural = "Publicacion"

class Link_archivo(models.Model):
	id_link = models.AutoField(primary_key=True)
	url_link = models.CharField(max_length=200, unique= True)
	titulo_link = models.CharField(max_length=200)
	fecha_link = models.DateTimeField(auto_now=True)
	publicacion = models.ForeignKey(Publicacion)
	class Meta:
		verbose_name = "Link_archivo"
		verbose_name_plural = "Link_archivo"
