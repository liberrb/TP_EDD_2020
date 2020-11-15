import scrapy
from datetime import datetime
import re
from spiders.items import Items
from nltk.corpus import stopwords
from nltk import word_tokenize
from config import Config
from utils import Utils


class FravegaSpiderSpider(scrapy.Spider):
    name = 'fravega_spider'
    allowed_domains = ['www.fravega.com']
    start_urls = [ Config().get_start_url()['fravega'] ]
    utils = Utils()

    def __init__(self, target=None, tipo_busqueda=None, *args, **kwargs):
        super().__init__(**kwargs)
        self.target = target
        self.tipo_busqueda = tipo_busqueda

    def parse(self, response):
        links = response.xpath('//div[@class="Categories__StyledCategories-m0ao24-0 heNzOg"]/ul/li/a')
        for link in links:
            nombre = link.xpath(".//text()").get()
            link = link.xpath(".//@href").get()
                
            yield response.follow(url=link, callback=self.parse_categories)
                
    def parse_categories(self, response):
            
        links = response.xpath('//div[contains(@class,"contenidoCajas1")]/h3/a')
        for link in links:
            nombre = link.xpath(".//text()").get()
            link = link.xpath(".//@href").get()
                
            yield response.follow(url=link, callback=self.parse_productos)      

    def parse_productos(self, response):
        base_url= 'https://www.fravega.com'
        categoria = response.xpath('.//h1[@name="categoryTitle"]/text()').get()
        for products in response.xpath("//ul[@class='listingDesktopstyled__SearchResultList-wzwlr8-6 fCKkuk']/li"):
            
            #title
            title = products.xpath(".//div/a/article/div/h4/text()[2]").get()
            
            #price
            precio = products.xpath('.//div/a/article/div/div/span/text()').get()

            price = 0
            if precio:
                price = precio.replace('$','')
                price = price.replace('.', '').strip()
                price = price.replace(',', '.')
                price = float(price)

            #fecha y hora de extraccion
            now = datetime.now()
            dt_format = now.strftime("%d/%m/%Y %H:%M:%S")

            product_link = base_url + products.xpath(".//div/a/@href").get()

            entra_yield = False
            
            if self.tipo_busqueda == '1':
                entra_yield = self.utils.tipo_busqueda_1(self.target, title)
                
            elif self.tipo_busqueda == '2':
                entra_yield = self.utils.tipo_busqueda_2(self.target, title)

            elif self.tipo_busqueda == '3':
                entra_yield = self.utils.tipo_busqueda_3(self.target, title)

            if entra_yield:

                item = Items()
                item['title'] = title
                item['categoria'] = categoria
                item['price'] = price
                item['link'] = product_link 
                item['fecha'] = dt_format
                item['market'] = 'fravega'

                yield item
            
            
            
            
            