# -*- coding: utf-8 -*
import scrapy
from scrapy.item import Item, Field
from scrapy_djangoitem import DjangoItem
from WB_app.models import Autor,Publicacion

class PublicacionItem(DjangoItem):
	django_model = Publicacion
	nombre_autor = scrapy.Field()
	url_link = scrapy.Field()

class AutorItem(DjangoItem):
	django_model = Autor
