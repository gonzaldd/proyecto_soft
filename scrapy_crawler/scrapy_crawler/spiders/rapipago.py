import scrapy
from scrapy_crawler.items import OfficeItem

class RapiPagoSpider(scrapy.Spider):
    name = "rapipago"
    allowed_domains = ["rapipago.com.ar"]
    start_urls = [
        "http://www.rapipago.com.ar/rapipagoWeb/index.htm",
    ]

    def parse(self, response):
        for idx, province in enumerate(response.xpath("//*[@id='provinciaSuc']/option")):
            if idx > 0: # avoid select prompt
                code = province.xpath('@value').extract()
                request = scrapy.FormRequest("http://www.rapipago.com.ar/rapipagoWeb/suc-buscar.htm",
                                             formdata={'palabraSuc': 'Por palabra', 'provinciaSuc': code},
                                             callback=self.parse_province)

                request.meta['province'] = province.xpath('text()').extract()[0]
                request.meta['province_code'] = code
                yield request

    def parse_province(self, response):
        for idx, city in enumerate(response.xpath("//*[@id='ciudadSuc']/option")):
            if idx > 0: 
                code = city.xpath('@value').extract()[0]

                request = scrapy.FormRequest("http://www.rapipago.com.ar/rapipagoWeb/suc-buscar.htm",
                                             formdata={'palabraSuc': 'Por palabra',
                                                       'provinciaSuc': response.meta['province_code'],
                                                       'ciudadSuc': code},
                                             callback=self.parse_city)

                request.meta['province'] = response.meta['province']
                request.meta['province_code'] = response.meta['province_code']
                request.meta['city'] = city.xpath('text()').extract()[0]
                request.meta['city_code'] = code
                yield request

    def parse_city(self, response):
        for link in response.xpath("//a[contains(@href,'index?pageNum')]/@href").extract():
            request = scrapy.FormRequest('http://www.rapipago.com.ar/rapipagoWeb/suc-buscar.htm?' + link.split('?')[1],
                                         formdata={'palabraSuc': 'Por palabra',
                                                   'provinciaSuc': response.meta['province_code'],
                                                   'ciudadSuc': response.meta['city_code']},
                                         callback=self.parse_city_data)

            request.meta['province'] = response.meta['province']
            request.meta['city'] = response.meta['city']

            yield request

    def parse_city_data(self, response):
        # TODO: follow page links (7)
        for office in response.xpath("//*[@class='resultadosNumeroSuc']"):
            officeItem = OfficeItem()
            officeItem['province'] = response.meta['province']
            officeItem['city'] = response.meta['city']
            officeItem['name'] = office.xpath("../*[@class='resultadosTextWhite']/text()").extract()[0]
            officeItem['address'] = office.xpath("../..//*[@class='resultadosText']/text()").extract()[0]
            yield officeItem