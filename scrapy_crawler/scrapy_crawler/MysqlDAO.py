# -*- coding: utf-8 -*-
import re
from WB_app.models import Autor,Publicacion,Link_archivo
import django
django.setup()#Sin esto, no anda el Many to many 

class ScrapAutores(object):

	def process_item(self, item, spider):
		try:
			autor = Autor.objects.get(nombre_comp_autor = item['nombre_autor'])
			try:
				p = Publicacion.objects.get(titulo_publicacion= item['titulo_publicacion'])
				p.autores.add(autor)
			except:
				p = Publicacion(titulo_publicacion= item['titulo_publicacion'],
					anio_publicacion= item['anio_publicacion'],
					isbn = item['isbn']
					)
				p.save()
				p.autores.add(autor)
		except:
			print("No Existe el autor, sera guardado.")
			autor = Autor(nombre_comp_autor = item['nombre_autor'])
			autor.save()
			try:
				p = Publicacion.objects.get(titulo_publicacion= item['titulo_publicacion'])
				p.autores.add(autor)	
			except:
				p = Publicacion(titulo_publicacion= item['titulo_publicacion'],
					anio_publicacion= item['anio_publicacion'],
					isbn = item['isbn']
					)
				p.save()
				p.autores.add(autor)
		return item