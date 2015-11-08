# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy_crawler.items import AutorItem, PublicacionItem
from scrapy.linkextractors import LinkExtractor

class crawler(scrapy.Spider):
	name = "crawler"
	allowed_domains = ["rinfi.fi.mdp.edu.ar",
						"www.sac.org.ar",
						"reiec.sites.exa.unicen.edu.ar"]
	start_urls = ["http://www.sac.org.ar/argentine-cardiology-journal-archive",
					"http://rinfi.fi.mdp.edu.ar/xmlui/recent-submissions",
					"http://reiec.sites.exa.unicen.edu.ar/que-es-reiec-1"]

	#rules = (#Rule(LinkExtractor(allow=['/v26n3\.html']), callback='parse'),
			 #Rule(LinkExtractor(allow=['/?numero=28525']), callback='parse_web2'))

	def parse(self, response):
		for href in response.css("a::attr('href')"):
			print href
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_web1)

	def parse_web1(self, response):
		'''for sel in response.xpath("//div[@id='sites-canvas-main-content']/div[@class='sites-layout-name-right-sidebar-hf sites-layout-vbox']"):
			print (sel.xpath("//div[@id='sites-canvas-main-content']/div[@class='sites-layout-name-right-sidebar-hf sites-layout-vbox']/div/div/div") )
			print("HEY HEY")'''
		'''for sel in response.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']"):
			publicacion = PublicacionItem()
			print (sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_artifactbrowser_ItemViewer_div_item-view']/div[@class='item-summary-view-metadata']/h1/text()").extract()[0].strip())#titulo
			print( response.xpath("//meta[@name='citation_date']/@content").re(r'\d\d\d\d')[0].strip())#Anio
			print( response.xpath("//meta[@name='citation_isbn']/@content").extract()[0])#isbn
			#print (sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_artifactbrowser_ItemViewer_div_item-view']/div[@class='item-summary-view-metadata']/div[@class='simple-item-view-authors']") Nombre autor
			print( response.xpath("//meta[@scheme='DCTERMS.URI']/@content").extract()[0])#url base
			print (sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_artifactbrowser_ItemViewer_div_item-view']/div/div/div/a[@class='image-link']/@href").extract()[0].strip())#link'''

		i=0
		for sel in response.xpath("//ul[@class='d3s-revista']"):
			publicaciones = sel.xpath("//li[contains(p, 'Scientific Letters')]/p[@class='d3s-titulo-post']/text()").extract()
			autores = sel.xpath("//li[contains(p, 'Scientific Letters')]/p[@class='d3s-titulo-autores']/text()").extract()
			links = sel.xpath("////li[contains(p, 'Scientific Letters')]/a[contains(@href,'.pdf')]/@href").extract()
			if i == 0:
				o=0
				while o != len(publicaciones):
					publicacion = PublicacionItem()
					publicacion['titulo_publicacion'] = publicaciones[o]
					publicacion['anio_publicacion'] = response.xpath("//p[@class='d3s-titulo-numero']/text()").re(r'\d\d\d\d')[0].strip()
					publicacion['isbn'] = response.xpath("//div[@id='d3s-page-content']/div/div/div/text()").re(r'\d\d\d\d-\d\d\d\d')[0].strip()
					publicacion['nombre_autor'] = autores[o]
					publicacion['url_link'] = links[o]
					yield publicacion
					o+=1
				i+=1

		'''for sel in response.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']"):
			publicacion = PublicacionItem()
			print (sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_artifactbrowser_ItemViewer_div_item-view']/div[@class='item-summary-view-metadata']/h1/text()").extract()[0].strip())#titulo
			print( response.xpath("//meta[@name='citation_date']/@content").re(r'\d\d\d\d')[0].strip())#Anio
			print( response.xpath("//meta[@name='citation_isbn']/@content").extract()[0])#isbn
			#print (sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_artifactbrowser_ItemViewer_div_item-view']/div[@class='item-summary-view-metadata']/div[@class='simple-item-view-authors']") Nombre autor
			print( response.xpath("//meta[@scheme='DCTERMS.URI']/@content").extract()[0])#url base
			print (sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_artifactbrowser_ItemViewer_div_item-view']/div/div/div/a[@class='image-link']/@href").extract()[0].strip())#link'''


		'''for sel in response.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']"):
			publicacion = PublicacionItem()
			print (sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_artifactbrowser_ItemViewer_div_item-view']/div[@class='item-summary-view-metadata']/h1/text()").extract()[0].strip())#titulo
			print( response.xpath("//meta[@name='citation_date']/@content").re(r'\d\d\d\d')[0].strip())#Anio
			print( response.xpath("//meta[@name='citation_isbn']/@content").extract()[0])#isbn
			#print (sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_artifactbrowser_ItemViewer_div_item-view']/div[@class='item-summary-view-metadata']/div[@class='simple-item-view-authors']") Nombre autor
			print( response.xpath("//meta[@scheme='DCTERMS.URI']/@content").extract()[0])#url base
			print (sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_artifactbrowser_ItemViewer_div_item-view']/div/div/div/a[@class='image-link']/@href").extract()[0].strip())#link'''
