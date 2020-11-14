import scrapy
import re


class CetrogarSpiderSpider(scrapy.Spider):
    name = 'cetrogar_spider'
    allowed_domains = ['www.cetrogar.com.ar']
    start_urls = ['https://www.cetrogar.com.ar/']
    
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
        
        categoria = response.xpath('//span[@class="base"]/text()')
        for product in response.xpath("//ol[@class='products list items product-items  defer-images-grid']/li"):
            titulo = product.xpath(".//a[@class='product-item-link']/text()").get()
            price = product.xpath('.//span[@class="price-container price-final_price tax weee"]/span[@data-price-type="finalPrice"]/span[@class="price"]/text()').get()
            titulo = titulo.strip().lower()
            
            #fecha y hora de extraccion
            now = datetime.now()
            dt_format = now.strftime("%d/%m/%Y %H:%M:%S")
            
            #link del producto
            product_link=response.xpath("/a[@class='product-item-link']/@href")

            entra_yield = False
            
            if self.tipo_busqueda == 1:
                pass #armar el re
                
            elif self.tipo_busqueda == 2:
                pass #armar el re
            
            else: #seria opcion3
                if re.findall(r"(?=("+'|'.join(self.target)+r"))",title.lower()):
                    entra_yield = True

            if entra_yield:
                item = Items()
                item['title'] = title
                item['categoria'] = categoria
                item['price'] = price
                item['link'] = product_link 
                item['fecha'] = dt_format

                yield item
        
        next_page = response.xpath('//a[@class="action  next"]/@href').get()
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_productos)