from django.db import models

class oficina(models.Model):
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = "oficina"
        verbose_name_plural = "oficina"

class Nombre(models.Model):
	nombre = models.CharField(max_length=10)