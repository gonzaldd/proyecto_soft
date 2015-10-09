import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy_crawler.items import AutorItem, Publicacion
from scrapy.linkextractors import LinkExtractor

class crawler(scrapy.Spider):
	name = "crawler"
	allowed_domains = ["actaodontologicalat.com",
						"www.sac.org.ar"]
	start_urls = ["http://www.sac.org.ar/argentine-cardiology-journal-archive",]

	#rules = (#Rule(LinkExtractor(allow=['/v26n3\.html']), callback='parse'),
			 #Rule(LinkExtractor(allow=['/?numero=28525']), callback='parse_web2'))

	def parse(self, response):
		for href in response.css("a::attr('href')"):
			print href
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_web1)
#		'''for sel in response.xpath("//td/p/span[@style='font-style: italic; font-size: 11px' or @style='font-size: 11px; font-style: italic']"):
#			autor = AutorItem()
#			nombre = sel.xpath("text()[normalize-space()]").extract()
#			autor['nombre_comp_autor'] = nombre[0].strip('\t\r\n')
#			yield autor
#		return'''

	def parse_web1(self, response):
		for sel in response.xpath("//ul[@class='d3s-revista']/li"):
			tipo = sel.xpath("p[@class='d3s-titulo-seccion']/text()[normalize-space()]").extract()
			if "Scientific Letters" in tipo[0]:
				print tipo[0].strip()
				autor = AutorItem()
				autor['nombre_comp_autor'] = nombre = sel.xpath("//ul/li/p[@class='d3s-titulo-autores']/text()").extract()[0].strip()
				return autor