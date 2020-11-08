import scrapy
from datetime import datetime

#para correrlo uso el comando scrapy runspider casa_audio_spider.py -O output.json

class CasaDelAudioSpider(scrapy.Spider):
    name = 'casa_audio_spider'
    allowed_domain = ['www.casadelaudio.com/']
    start_urls = ['https://www.casadelaudio.com/']
    
    def parse(self, response):
        links = response.xpath('//ul[@class="dropdown-menu"]/li/ul/li/a')
        for link in links:
            link = link.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_productos)

    def parse_productos(self, response):
        base_url = 'https://www.casadelaudio.com'
        categoria = response.xpath('//h1[@class="hidden-xs"]/text()').get() 
        for product in response.xpath('//ul[@class="row"]/li/article'): 
            
            #title
            title = product.xpath('normalize-space(.//input/@data-pname)').get()

            #armo el precio
            #moneda = product.xpath('./div[@class="box_data"]/a/div[@class="price_wrapper"]/div[@class="hidden-xs price"]/strong/text()').get()
            valor = product.xpath('./div[@class="box_data"]/a/div[@class="price_wrapper"]/div[@class="hidden-xs price"]/strong/span/text()').get()
            #price = moneda + valor
            price = float(valor)

            #fecha y hora de extraccion
            now = datetime.now()
            dt_format = now.strftime("%d/%m/%Y %H:%M:%S")
            
            #link de producto
            product_link = base_url + product.xpath('.//div[@class="box_data"]/a/@href').get()
            
            yield {
                'title': title,
                'categoria': categoria,
                'price': price,
                'link': product_link, 
                'fecha': dt_format
            }
