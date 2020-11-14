import scrapy
from datetime import datetime
import re
from spiders.items import Items
from nltk.corpus import stopwords
from nltk import word_tokenize


class MusimundoSpider(scrapy.Spider):
    name = 'musimundo_spider'
    allowed_domain = ['www.musimundo.com']
    start_urls = ['https://www.musimundo.com/']
        
    def __init__(self, target=None, tipo_busqueda=None, *args, **kwargs):
        super().__init__(**kwargs)
        self.target = target
        self.tipo_busqueda = tipo_busqueda

    def parse(self, response):
        links = response.xpath('//div[@class="navigationbarcollectioncomponent"]/div[@class="container"]/ul[@class="mus-navUl clear_fix"]/li/div/ul/li/div/div/h2/a')
        for link in links:
            link = link.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.parse_productos)

    def parse_productos(self, response):
        base_url = 'https://www.musimundo.com'
        categoria = response.xpath('normalize-space(//div[@class="col span_9"]/div[@class="searchResultsGridComponent"]/div[@class="mus-results-title"]/h1/text())').get() 
        for product in response.xpath('//div[@class="productGrid clearfix"]/div/div/div/a'):
            
            #title
            title = product.xpath('normalize-space(.//div[@class="mus-pro-desc"]/p[@class="mus-pro-name"]/text())').get()

            #armo el precio
            #moneda = product.xpath('.//div[@class="mus-pro-quotes"]/div/span[@class="mus-pro-quotes-currency strong"]/text()').get()
            entero = product.xpath('.//div[@class="mus-pro-quotes"]/div/span[@class="mus-pro-quotes-price strong"]/text()').get()
            decimal = product.xpath('.//div[@class="mus-pro-quotes"]/div/span[@class="mus-pro-quotes-decimals strong"]/text()').get()
            
            price = 0
            if entero:
                valor = entero.replace('.', '') + decimal
                price = float(valor.replace(',', '.'))

            #fecha y hora de extraccion
            now = datetime.now()
            dt_format = now.strftime("%d/%m/%Y %H:%M:%S")
            
            #link de producto
            product_link = base_url + product.xpath('.//@href').get()
            
            entra_yield = False
            
            if self.tipo_busqueda == '1':
                entra_yield = title.lower() == self.target
                
            elif self.tipo_busqueda == '2':
                stop_words = frozenset(stopwords.words('spanish'))
                title_tokens = word_tokenize(title.lower())
                title_token = [w for w in title_tokens if not w in stop_words]
                entra_yield =  all(item in self.target for item in title_token)
            
            elif self.tipo_busqueda == '3':
                if re.findall(r"(?=("+'|'.join(self.target)+r"))",title.lower()):
                    entra_yield = True

            if entra_yield:
                item = Items()
                item['title'] = title
                item['categoria'] = categoria
                item['price'] = price
                item['link'] = product_link 
                item['fecha'] = dt_format
                item['market'] = 'musimundo'

                yield item
                
        next_page = response.xpath('//li[@class="next square not-border"]/a/@href').get()
        if next_page:
            next_page = base_url+next_page
            yield scrapy.Request(url=next_page, callback=self.parse_productos)
