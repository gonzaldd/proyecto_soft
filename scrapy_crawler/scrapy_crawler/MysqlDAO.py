# -*- coding: utf-8 -*-
import re
from WB_app.models import Autor,Publicacion,Link_archivo
import django
django.setup()#Sin esto, no anda el Many to many 

class ScrapAutores(object):

	def process_item(self, item, spider):
		try:
			p = Publicacion.objects.get(titulo_publicacion= item['titulo_publicacion'])
			try:
				l = Link_archivo.objects.get(titulo_link = item['url_link'])
				print("Ya existe")
			except Exception as e:
				print "Exception: ", e
				l = Link_archivo(url_link=item['url_link'],
					titulo_link = item['titulo_publicacion'],
					publicacion = p
				)
				l.save()
			for s in item['nombre_autor'].split(','):
				print(s)
				try:
					autor = Autor.objects.get(nombre_comp_autor = s)
					p.autores.add(autor)
					print(autor)
				except Exception as e:
					print 'EXCEPCION: ',e
					print("No Existe el autor, sera guardado.")
					autor = Autor(nombre_comp_autor = s)
					autor.save()
					p.autores.add(autor)

		except Exception as e:
			print "Exception: " ,e
			p = Publicacion(titulo_publicacion= item['titulo_publicacion'],
					anio_publicacion= item['anio_publicacion'],
					isbn = item['isbn']
					)
			p.save()
			try:
				l = Link_archivo.objects.get(titulo_link = item['url_link'])
				print("Ya existe")
			except Exception as e:
				print "Exception: ", e
				l = Link_archivo(url_link=item['url_link'],
					titulo_link = item['titulo_publicacion'],
					publicacion = p
				)
				l.save()
			for s in item['nombre_autor'].split(','):
				print(s)
				try:
					autor = Autor.objects.get(nombre_comp_autor = s)
					p.autores.add(autor)
				except Exception as e:
					print 'Exception: ',e
					autor = Autor(nombre_comp_autor = s)
					autor.save()
					p.autores.add(autor)
