import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pruebas.items import PruebasItem


class PruebaSpider(CrawlSpider):
    name = 'prueba'
    allowed_domain = ['www.musimundo.com']
    start_urls = ['https://www.musimundo.com/telefonia/telefonos-celulares/c/82']

    rules = {
        Rule( LinkExtractor( allow=(), restrict_xpaths= ('//div[@class="mus-product-box-out"]')), callback = 'parse_item', follow=False )
    }

    def parse_item(self, response):
        c_item = PruebasItem()

        c_item['titulo'] = response.xpath('normalize-space(//p[@class="mus-pro-name strong"]/text())').extract()
        c_item['precio'] = response.xpath('//*[@id="productPageDetailsId"]/div/div[2]/div/div[1]/div[2]/div/span[2]/text()').extract()
        yield c_item


        
