# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy_crawler.items import AutorItem, PublicacionItem
from scrapy.linkextractors import LinkExtractor



class crawler(scrapy.Spider):
	name = "crawler"

	
	start_urls = ["http://www.sac.org.ar/argentine-cardiology-journal/",
					"http://rinfi.fi.mdp.edu.ar/xmlui/recent-submissions?offset=",
					"http://road.issn.org/issn_search?afs:query=&show-adv=0&afs:replies=100#.VqaLtl4oDtR",
					"http://www.intechopen.com/books/latest/1/list",
					"http://eprints.internano.org",
					"http://nparc.cisti-icist.nrc-cnrc.gc.ca/npsi/ctrl",
					"http://eprints.bbk.ac.uk/view/subjects/csis.html",
					"http://create.canterbury.ac.uk/view/subjects/QA75.html",
					"http://www.repository.heartofengland.nhs.uk/view/subjects/WK.html",
					"http://binpar.caicyt.gov.ar/cgi-bin/koha/opac-detail.pl?biblionumber=98723",
					"https://ueaeprints.uea.ac.uk/cgi/search/simple?exp=0|1|date/creators_name/title|archive|-|q:_fulltext_/abstract/creators_search_name/date/title:ALL:IN:fulltext|-|eprint_status:eprint_status:ALL:EQ:archive|metadata_visibility:metadata_visibility:ALL:EX:show&_action_search=1&order=date/creators_name/title&screen=Public::EPrintSearch&cache=2594200&search_offset=0",
					"http://search.scielo.org/?q=science&lang=pt&count=50&from=0&output=site&sort=&format=summary&fb=&page=1"]

	

	def parse(self, response):

		url0 = "http://www.sac.org.ar/argentine-cardiology-journal/"
		yield scrapy.Request(url0, callback=self.parse_web0)

		i=0
		urlP="http://rinfi.fi.mdp.edu.ar/xmlui/recent-submissions?offset="
		while(i<=40):
			urlP += `i`
			yield scrapy.Request(urlP,callback=self.parse_web1)
			i +=20
			urlP = "http://rinfi.fi.mdp.edu.ar/xmlui/recent-submissions?offset="
			
		url3 = "http://road.issn.org/issn_search?afs:query=&show-adv=0&afs:replies=100#.VqaLtl4oDtR"
		yield scrapy.Request(url3,callback=self.parse_web2)
				
		j=1
		urlB1 = "http://www.intechopen.com/books/latest/"
		urlB2 = "/list"
		while(j<=188):
			urlB1 += `j`
			urlB1 += urlB2
			yield scrapy.Request(urlB1,callback=self.parse_web3) 
			j+=1
			urlB1 = "http://www.intechopen.com/books/latest/"

		url5 = "http://eprints.internano.org"
		yield scrapy.Request(url5,callback=self.parse_web4)
		url6 = "http://nparc.cisti-icist.nrc-cnrc.gc.ca/npsi/ctrl"
		yield scrapy.Request(url6,callback=self.parse_web5)
		url7 = "http://eprints.bbk.ac.uk/view/subjects/csis.html"
		yield scrapy.Request(url7,callback=self.parse_web6)
		url8 = "http://create.canterbury.ac.uk/view/subjects/QA75.html"
		yield scrapy.Request(url8,callback=self.parse_web7)
		url9 = "http://www.repository.heartofengland.nhs.uk/view/subjects/WK.html"
		yield scrapy.Request(url9,callback=self.parse_web8)
		

		f=98723
		urlF="http://binpar.caicyt.gov.ar/cgi-bin/koha/opac-detail.pl?biblionumber="
		while(f<=99500): 
			urlF += `f`
			yield scrapy.Request(urlF,callback=self.parse_web9)
			f +=1
			urlF = "http://binpar.caicyt.gov.ar/cgi-bin/koha/opac-detail.pl?biblionumber="
		
		url10 = "https://ueaeprints.uea.ac.uk/cgi/search/simple?exp=0|1|date/creators_name/title|archive|-|q:_fulltext_/abstract/creators_search_name/date/title:ALL:IN:fulltext|-|eprint_status:eprint_status:ALL:EQ:archive|metadata_visibility:metadata_visibility:ALL:EX:show&_action_search=1&order=date/creators_name/title&screen=Public::EPrintSearch&cache=2594200&search_offset=0"
		yield scrapy.Request(url10,callback=self.parse_web10)

		q=1
		a = 1
		urlQ = 'http://search.scielo.org/?q=science&lang=pt&count=50&from=1&output=site&sort=&format=summary&fb=&page='
		while(q<=10): 

			urlQ += `q`
			yield scrapy.Request(urlQ,callback=self.parse_web11)
			q+=1
			a = a+50
			urlQ = 'http://search.scielo.org/?q=science&lang=pt&count=50&from='
			urlQ += str(a)
			urlQ += '&output=site&sort=&format=summary&fb=&page='
		
		

		


	def parse_web0(self, response): #http://www.sac.org.ar/argentine-cardiology-journal/
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
		
	def parse_web1(self, response): #http://rinfi.fi.mdp.edu.ar/xmlui/recent-submissions?offset=0/20/40
		i=0
		for sel in response.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']"):
			publicaciones = sel.xpath("//div[@id='ds-body']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_main-recent-submissions']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_recent-submissions']/ul[@class='ds-artifact-list']/li[@class='ds-artifact-item odd' or @class='ds-artifact-item even']/div[@class='artifact-description']/div[@class='artifact-title']/a/text()").extract()
			#publicaciones = sel.xpath("//div[@id='ds-body']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_main-recent-submissions']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_recent-submissions']/ul[@class='ds-artifact-list']/li[@class='ds-artifact-item even']/div[@class='artifact-description']/div[@class='artifact-title']/a/text()").extract()
			autores = sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_main-recent-submissions']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_recent-submissions']/ul[@class='ds-artifact-list']/li[@class='ds-artifact-item odd']/div[@class='artifact-description']/div[@class='artifact-info']/span[@class='author']/span/text()").extract()
			links = sel.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_main-recent-submissions']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_recent-submissions']/ul[@class='ds-artifact-list']/li[@class='ds-artifact-item odd']/div[@class='artifact-description']/div[@class='artifact-title']/a/@href").extract()
			if i == 0:
				o=0
				while o != len(publicaciones):
					publicacion = PublicacionItem()
					publicacion['titulo_publicacion'] = publicaciones[o]
					publicacion['anio_publicacion'] = (response.xpath("//div[@id='ds-main']/div[@id='ds-content-wrapper']/div[@id='ds-content']/div[@id='ds-body']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_main-recent-submissions']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_recent-submissions']/ul[@class='ds-artifact-list']/li[@class='ds-artifact-item odd']/div[@class='artifact-description']/div[@class='artifact-info']/span[@class='publisher-date']/span[@class='date']/text()").re(r'\d\d\d\d')[0].strip())
					publicacion['isbn'] = "Null"
					publicacion['nombre_autor'] = autores[o]
					publicacion['url_link'] = "http://rinfi.fi.mdp.edu.ar"+ links[o]
					yield publicacion
					o+=1
				i+=1
		

	def parse_web2(self, response): #http://road.issn.org/issn_search?afs:query=&show-adv=0&afs:replies=100#.VrO8GF4oDtT
		i=0
		for sel in response.xpath("//div[@class='page-container']/div[@class='page']/div[@id='main-content']/div[@class='main-content-inside']/div[@class='region-content']/div[@class='issn-search']/div[@class='search-results']/div[@class='search-result type-journals']"):
			publicaciones = sel.xpath("//div[@class='page-container']/div[@class='page']/div[@id='main-content']/div[@class='main-content-inside']/div[@class='region-content']/div[@class='issn-search']/div[@class='search-results']/div[@class='search-result type-journals']/div[@class='search-result-title']/a/text()").extract()
			#publicaciones = sel.xpath("//div[@id='ds-body']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_main-recent-submissions']/div[@id='aspect_discovery_recentSubmissions_RecentSubmissionTransformer_div_recent-submissions']/ul[@class='ds-artifact-list']/li[@class='ds-artifact-item even']/div[@class='artifact-description']/div[@class='artifact-title']/a/text()").extract()
			autores = sel.xpath("//div[@class='page-container']/div[@class='page']/div[@id='main-content']/div[@class='main-content-inside']/div[@class='region-content']/div[@class='issn-search']/div[@class='search-results']/div[@class='search-result type-journals']/div[@class='search-result-publisher']/text()").extract()
			links = sel.xpath("//div[@class='page-container']/div[@class='page']/div[@id='main-content']/div[@class='main-content-inside']/div[@class='region-content']/div[@class='issn-search']/div[@class='search-results']/div[@class='search-result type-journals']/div[@class='search-result-title']/a/@href").extract()
			anios = response.xpath("//div[@class='page-container']/div[@class='page']/div[@id='main-content']/div[@class='main-content-inside']/div[@class='region-content']/div[@class='issn-search']/div[@class='search-results']/div[@class='search-result type-journals']/div[@class='search-result-registration_year']").re(r'\d\d\d\d-\d\d-\d\d')
			isbns = response.xpath("//div[@class='page-container']/div[@class='page']/div[@id='main-content']/div[@class='main-content-inside']/div[@class='region-content']/div[@class='issn-search']/div[@class='search-results']/div[@class='search-result type-journals']/div[@class='search-result-issn']").re(r'\d+-\d+')
			if i == 0:
				o=0
				while o != len(publicaciones):
					publicacion = PublicacionItem()
					publicacion['titulo_publicacion'] = publicaciones[o]
					publicacion['anio_publicacion'] = anios[o]
					publicacion['isbn'] = isbns[o]
					publicacion['nombre_autor'] = autores[o]
					publicacion['url_link'] = links[o]
					yield publicacion
					o+=1
				i+=1
	
	
	def parse_web3(self, response): #http://www.intechopen.com/books/latest/1/list itera sobre todas las paginas.
		i=0
		for sel in response.xpath("//div[@id='sizer']/div[@id='content']/div[@class='grid']/div[@class='main-content']/div[@id='tc']/div/ul[@class='book-listing entity-listing']/li"):
			publicaciones = sel.xpath("//div[@id='sizer']/div[@id='content']/div[@class='grid']/div[@class='main-content']/div[@id='tc']/div/ul[@class='book-listing entity-listing']/li/dl/dt/a/text()").extract() #publicacion
			autores = response.xpath("//div[@id='sizer']/div[@id='content']/div[@class='grid']/div[@class='main-content']/div[@id='tc']/div/ul[@class='book-listing entity-listing']/li/dl/dd[@class='meta']/text()[count(preceding-sibling::br) = 0]").re(r'Editor\s*(.*)') #FUNCIONA!
			links = sel.xpath("//div[@id='sizer']/div[@id='content']/div[@class='grid']/div[@class='main-content']/div[@id='tc']/div/ul[@class='book-listing entity-listing']/li/dl/dt/a/@href").extract() #links
			anios = response.xpath("//div[@id='sizer']/div[@id='content']/div[@class='grid']/div[@class='main-content']/div[@id='tc']/div/ul[@class='book-listing entity-listing']/li/dl/dd[@class='meta']/text()").re(r' \d\d\d\d')
			isbns = response.xpath("//div[@id='sizer']/div[@id='content']/div[@class='grid']/div[@class='main-content']/div[@id='tc']/div/ul[@class='book-listing entity-listing']/li/dl/dd[@class='meta']/text()").re(r'\d\d\d-\d\d\d-\d\d-\d\d\d\d-\d')
			if i == 0:
				o=0
				while o != len(publicaciones):
					publicacion = PublicacionItem()
					publicacion['titulo_publicacion'] = publicaciones[o]
					publicacion['anio_publicacion'] = anios[o]
					publicacion['isbn'] = isbns[o]
					publicacion['nombre_autor'] = autores[o]
					publicacion['url_link'] = "http://www.intechopen.com"+links[o]
					yield publicacion
					o+=1
				i+=1	


	def parse_web4(self, response): #http://eprints.internano.org/
		i=0
		for sel in response.xpath("//div[@id='wrapper']/div[@id='shadow']/div[@id='box']/div"):
			publicaciones = sel.xpath("//div[@id='wrapper']/div[@id='shadow']/div[@id='box']/div/div[@class='ep_tm_page_content']/div[@class='ep_latest_additions']/div[@class='ep_latest_list']/div[@class='ep_latest_result']/a/em/text()").extract() #publicacion
			autores = response.xpath("//div[@id='wrapper']/div[@id='shadow']/div[@id='box']/div/div[@class='ep_tm_page_content']/div[@class='ep_latest_additions']/div[@class='ep_latest_list']/div[@class='ep_latest_result']/span[@class='person_name']/text()").extract() #Autor
			links = sel.xpath("//div[@id='wrapper']/div[@id='shadow']/div[@id='box']/div/div[@class='ep_tm_page_content']/div[@class='ep_latest_additions']/div[@class='ep_latest_list']/div[@class='ep_latest_result']/a/@href").extract()
			anios = response.xpath("//div[@id='wrapper']/div[@id='shadow']/div[@id='box']/div/div[@class='ep_tm_page_content']/div[@class='ep_latest_additions']/div[@class='ep_latest_list']/div[@class='ep_latest_result']/text()").re(r'\((\d\d\d\d)\)')
			isbns = response.xpath("//div[@id='wrapper']/div[@id='shadow']/div[@id='box']/div/div[@class='ep_tm_page_content']/div[@class='ep_latest_additions']/div[@class='ep_latest_list']/div[@class='ep_latest_result']/text()").re(r'\d+-\d+|\w+-\w+')
			if i == 0:
				o=0
				while o != len(publicaciones):
					publicacion = PublicacionItem()
					publicacion['titulo_publicacion'] = publicaciones[o]
					publicacion['anio_publicacion'] = anios[o]
					publicacion['isbn'] = isbns[o]
					publicacion['nombre_autor'] = autores[o]
					publicacion['url_link'] = links[o]
					yield publicacion
					o+=1
				i+=1
	
	def parse_web5(self, response): #http://nparc.cisti-icist.nrc-cnrc.gc.ca/npsi/ctrl
		i=0
		for sel in response.xpath("//div[@class='page']/div[@class='core']/div[@class='colLayout']/div[@class='center']/div[@id='content-container-3col']"):
			publicaciones = sel.xpath("//div[@class='page']/div[@class='core']/div[@class='colLayout']/div[@class='center']/div[@id='content-container-3col']/div[@class='paddRecent']/div[@class='table-row widthFull']/span[@class='boldFont']/a/text()").extract() #publicacion
			autores = response.xpath("//div[@class='page']/div[@class='core']/div[@class='colLayout']/div[@class='center']/div[@id='content-container-3col']/div[@class='paddRecent']/div[@class='table-row widthFull forceWordWrap']/a/text()").extract() #Autor
			links = sel.xpath("//div[@class='page']/div[@class='core']/div[@class='colLayout']/div[@class='center']/div[@id='content-container-3col']/div[@class='paddRecent']/div[@class='table-row widthFull']/span[@class='boldFont']/a/@href").extract()
			if i == 0:
				o=0
				while o != len(publicaciones):
					publicacion = PublicacionItem()
					publicacion['titulo_publicacion'] = publicaciones[o]
					publicacion['anio_publicacion'] = 2016
					publicacion['isbn'] = "1059-9630"
					publicacion['nombre_autor'] = autores[o]
					publicacion['url_link'] = "http://nparc.cisti-icist.nrc-cnrc.gc.ca"+links[o]
					yield publicacion
					o+=1
				i+=1


	def parse_web6(self, response): #http://eprints.bbk.ac.uk/view/subjects/csis.html
		
		# Cada publicacion esta en un <p>. Hago el for sobre ellos.
		for publication in response.css('div > div.ep_tm_page_content > div.ep_view_page.ep_view_page_view_subjects > p'):

			# Cada publicacion tiene un <a> donde se encuentra el titulo y el Link.
			for title in publication.xpath('./a'):
				pubtitle = title.xpath('normalize-space(.)').extract_first()
				publink = title.xpath('@href').extract_first()
				break
			# Aplico Regex para sacar el Año entre los parentesis
			pubyear = publication.xpath('./text()').re_first(r'\((\d+)\)')

			# Obtengo los autores. Me devuelve un array, pero no lo puedo guardar asi en la base, y como no encontre solucion, decidi guardar uno solo.
			author = publication.xpath('./span[@class="person_name"][./following-sibling::a]/text()').extract()

			# Obtengo el numero luego de ISBN o ISSN. Si no hay nada, devuelve NULL
			isxn = publication.xpath('./a/following-sibling::text()').re_first(r'(ISBN\s+\d+|ISSN\s+\d+-\d+)')

			if isxn == None:
				isxn = "Null"
			
			publicacion = PublicacionItem()
			publicacion['titulo_publicacion'] = pubtitle
			publicacion['anio_publicacion'] = pubyear 
			publicacion['isbn'] = isxn
			publicacion['nombre_autor'] = author[0]
			publicacion['url_link'] = publink
			yield publicacion
			
	
	def parse_web7(self, response): #http://canterbury33.eprints-hosting.org/view/subjects/QA75.html
		for publication in response.css('div#ExtContainer > div#ExtWrapper > div#ExtBody > div#ExtMainContent > div.ep_view_page.ep_view_page_view_subjects > p'):

			# Cada publicacion tiene un <a> donde se encuentra el titulo y el Link.
			for title in publication.xpath('./a'):
				pubtitle = title.xpath('normalize-space(.)').extract_first()
				publink = title.xpath('@href').extract_first()
				break
			# Aplico Regex para sacar el Año entre los parentesis
			pubyear = publication.xpath('./text()').re_first(r'\((\d+)\)')

			# Obtengo los autores. Me devuelve un array, pero no lo puedo guardar asi en la base, y como no encontre solucion, decidi guardar uno solo.
			author = publication.xpath('./span[@class="person_name"][./following-sibling::a]/text()').extract()

			# Obtengo el numero luego de ISBN o ISSN. Si no hay nada, devuelve NULL
			isxn = publication.xpath('./a/following-sibling::text()').re_first(r'(ISBN\s+\d+|ISSN\s+\d+-\d+)')

			if isxn == None:
				isxn = "Null"
			
			publicacion = PublicacionItem()
			publicacion['titulo_publicacion'] = pubtitle
			publicacion['anio_publicacion'] = pubyear 
			publicacion['isbn'] = isxn
			publicacion['nombre_autor'] = author[0]
			publicacion['url_link'] = publink
			yield publicacion	
			
	def parse_web8(self, response): #Repository UK
		# Cada publicacion esta en un <p>. Hago el for sobre ellos.
		for publication in response.css('div > div.ep_tm_page_content > div.ep_view_page.ep_view_page_view_subjects > p'):

			# Cada publicacion tiene un <a> donde se encuentra el titulo y el Link.
			for title in publication.xpath('./a'):
				pubtitle = title.xpath('normalize-space(.)').extract_first()
				publink = title.xpath('@href').extract_first()
				break
			# Aplico Regex para sacar el Año entre los parentesis
			pubyear = publication.xpath('./text()').re_first(r'\((\d+)\)')

			# Obtengo los autores. Me devuelve un array, pero no lo puedo guardar asi en la base, y como no encontre solucion, decidi guardar uno solo.
			author = publication.xpath('./span[@class="person_name"][./following-sibling::a]/text()').extract()

			# Obtengo el numero luego de ISBN o ISSN. 
			

			isxn = publication.xpath('./a/following-sibling::text()').re_first(r'(ISBN\s+\d+|ISSN\s+\d+-\d+)')
			#IF para verificar si existe o no el ISBN. Sin este if, en la base se guarda un NULL (no un string que diga "null") por lo que solr no lo importa.
			if isxn == None:
				isxn = "Null"
			
			publicacion = PublicacionItem()
			publicacion['titulo_publicacion'] = pubtitle
			publicacion['anio_publicacion'] = pubyear 
			publicacion['isbn'] = isxn
			publicacion['nombre_autor'] = author[0]
			publicacion['url_link'] = publink
			yield publicacion
	
	def parse_web9(self, response): #Conicet!!
		
		for publication in response.css('div#wrap > div.main > div.container-fluid > div.row-fluid > div.span9 > div#catalogue_detail_biblio > div.record'):

			author = publication.xpath('./span[@class="results_summary publisher"]/span/span/a/text()').extract_first()
			title = publication.css("h1[property=name]::text").extract_first()
			issn = publication.css("span[property=issn]::text").extract_first()

			publicacion = PublicacionItem()
			publicacion['titulo_publicacion'] = title
			publicacion['anio_publicacion'] = "Null"
			publicacion['isbn'] = issn
			publicacion['nombre_autor'] = author
			publicacion['url_link'] = response.url
			yield publicacion
			
			
	def parse_web10(self, response): #https://ueaeprints.uea.ac.uk/cgi/search/simple?exp=0|1|date/creators_name/title|archive|-|q:_fulltext_/abstract/creators_search_name/date/title:ALL:IN:fulltext|-|eprint_status:eprint_status:ALL:EQ:archive|metadata_visibility:metadata_visibility:ALL:EX:show&_action_search=1&order=date/creators_name/title&screen=Public::EPrintSearch&cache=2594200&search_offset=0
		
		for publication in response.css('div#center > div#width > div#bodyWrap > div#centerCol > div#content > div.ep_search_results > table.ep_paginate_list > tr.ep_search_result'):

			author = publication.xpath('./td/span[@class="person_name"]/text()').extract_first()
			title = publication.xpath('./td/a/em/text()').extract_first()
			issn = publication.xpath('./td/text()').re_first(r'(ISBN\s+\d+|ISSN\s+\d+-\d+)')
			link = publication.xpath('./td/a/@href').extract_first()
			anio = publication.xpath('./td/text()').re_first(r'\((\d+)\)')

			if issn == None:
				issn = "Null"

			publicacion = PublicacionItem()
			publicacion['titulo_publicacion'] = title
			publicacion['anio_publicacion'] = anio
			publicacion['isbn'] = issn
			publicacion['nombre_autor'] = author
			publicacion['url_link'] = link
			yield publicacion
			
	def parse_web11(self, response): #Scielo
		
		for publication in response.css('div.results > div.item'):

			author = publication.xpath('./div[@class="col-md-11 col-sm-10 col-xs-11"]/div[@class="line authors"]/a/text()').extract_first()
			title = publication.xpath('./div[@class="col-md-11 col-sm-10 col-xs-11"]/div[@class="line"]/a/strong[@class="title"]/text()').extract_first()
			doi = publication.xpath('./div[@class="col-md-11 col-sm-10 col-xs-11"]/div[@class="line metadata"]/div[@class="col-md-12 col-sm-12"]/span/span/strong[@class="DOIResults"]/text()').extract_first()
			link = publication.xpath('./div[@class="col-md-11 col-sm-10 col-xs-11"]/div[@class="line"]/a/@href').extract_first()
			anio = publication.xpath('./div[@class="col-md-11 col-sm-10 col-xs-11"]/div[@class="line source"]/span/text()').re_first(r'\d\d\d\d')


			if doi == None:
				doi = "Null"
			else:
				doi = doi[4:]

			publicacion = PublicacionItem()
			publicacion['titulo_publicacion'] = title
			publicacion['anio_publicacion'] = anio
			publicacion['isbn'] = doi
			publicacion['nombre_autor'] = author
			publicacion['url_link'] = link
			yield publicacion
	
	
	
	