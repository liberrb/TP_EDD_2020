import scrapy
import re
from datetime import datetime
from spiders.items import Items
from nltk.corpus import stopwords
from nltk import word_tokenize
from config import Config
from utils import Utils


class CetrogarSpiderSpider(scrapy.Spider):
    name = 'cetrogar_spider'
    allowed_domains = ['www.cetrogar.com.ar']
    start_urls = [ Config().get_start_url()['cetrogar'] ]
    utils = Utils()
    
    def __init__(self, target='', **kwargs):
        super().__init__(**kwargs)  # python3
        self.target = target

    def parse(self, response):
        links = response.xpath('//div[@class="navigation-container"]/ul/li/a')
        for link in links:
            nombre = link.xpath(".//text()").get()
            link = link.xpath(".//@href").get()
            
            yield response.follow(url=link, callback=self.parse_productos)
            
    def parse_productos(self, response):
        
        categoria = response.xpath('//span[@class="base"]/text()').get()
        for product in response.xpath("//ol[@class='products list items product-items  defer-images-grid']/li"):
            title = product.xpath("normalize-space(.//a[@class='product-item-link']/text())").get()
            precio = product.xpath('.//span[@class="price-container price-final_price tax weee"]/span[@data-price-type="finalPrice"]/span[@class="price"]/text()').get()
            #title = titulo.strip().lower()
            
            #trabajo con los precios
            price = 0
            if precio:
                price = precio.replace('$','')
                price = price.replace('.', '')
                price = float(price)

            #fecha y hora de extraccion
            now = datetime.now()
            dt_format = now.strftime("%d/%m/%Y %H:%M:%S")
            
            #link del producto
            product_link = response.xpath(".//a[@class='product-item-link']/@href").get()

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
                item['market'] = 'cetrogar'

                yield item
        
        next_page = response.xpath('//a[@class="action  next"]/@href').get()
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_productos)