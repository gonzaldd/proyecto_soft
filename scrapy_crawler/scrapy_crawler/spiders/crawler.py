import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy_crawler.items import AutorItem, PublicacionItem
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

	def parse_web1(self, response):
		i=0
		for sel in response.xpath("//ul[@class='d3s-revista']"):
			publicaciones = sel.xpath("//li[contains(p, 'Scientific Letters')]/p[@class='d3s-titulo-post']/text()").extract()
			autores = sel.xpath("//li[contains(p, 'Scientific Letters')]/p[@class='d3s-titulo-autores']/text()").extract()
			if i == 0:
				o=0
				while o != len(publicaciones):
					for h in sel.xpath("//a[contains(@href,'.pdf')]/@href"):
						print h.extract()
					publicacion = PublicacionItem()
					publicacion['titulo_publicacion'] = publicaciones[o]
					publicacion['anio_publicacion'] = response.xpath("//p[@class='d3s-titulo-numero']/text()").re(r'\d\d\d\d')[0].strip()
					publicacion['isbn'] = response.xpath("//div[@id='d3s-page-content']/div/div/div/text()").re(r'\d\d\d\d-\d\d\d\d')[0].strip()
					publicacion['nombre_autor'] = autores[o]
					yield publicacion
					o+=1
				i+=1