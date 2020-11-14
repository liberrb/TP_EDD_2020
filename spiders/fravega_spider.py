import scrapy


class FravegaSpiderSpider(scrapy.Spider):
    name = 'fravega_spider'
    allowed_domains = ['www.fravega.com']
    start_urls = ['https://www.fravega.com/']

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
        categoria = response.xpath('//h1[@name="categoryTitle"]/text()']
        for products in response.xpath("//ul[@class='listingDesktopstyled__SearchResultList-wzwlr8-6 fCKkuk']/li"):
            
            #title
            title = products.xpath(".//div/a/article/div/h4/text()[2]").get(),
            
            price = products.xpath('.//div/a/article/div/div/span/text()').get()
           
           #fecha y hora de extraccion
            now = datetime.now()
            dt_format = now.strftime("%d/%m/%Y %H:%M:%S")

            link = base_url + products.path(".//div/a/@href")

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
            
            
            
            
            