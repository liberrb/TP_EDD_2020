import scrapy
from datetime import datetime
import re
from spiders.items import Items
from config import Config
from nltk.corpus import stopwords
from nltk import word_tokenize
from utils import Utils

class CasaDelAudioSpider(scrapy.Spider):
    name = 'casa_audio_spider'
    allowed_domain = ['www.casadelaudio.com/']
    start_urls = [ Config().get_start_url()['casa_del_audio'] ]
    utils = Utils()

    def __init__(self, target=None, tipo_busqueda=None, *args, **kwargs):
        super().__init__(**kwargs)
        self.target = target
        self.tipo_busqueda = tipo_busqueda
    
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
                item['market'] = 'casadelaudio'

                yield item
