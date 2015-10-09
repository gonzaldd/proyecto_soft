# -*- coding: utf-8 -*
import scrapy
from scrapy.item import Item, Field
from scrapy_djangoitem import DjangoItem
from WB_app.models import Autor,Publicacion,oficina

class OfficeItem(DjangoItem):
    django_model = oficina

class Publicacion(DjangoItem):
	django_model = Publicacion

class AutorItem(DjangoItem):
	django_model = Autor