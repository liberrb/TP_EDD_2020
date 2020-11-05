import scrapy


class CetrogarSpiderSpider(scrapy.Spider):
    name = 'cetrogar_spider'
    allowed_domains = ['www.cetrogar.com.ar']
    start_urls = ['https://www.cetrogar.com.ar/']

    def parse(self, response):
        links = response.xpath('//div[@class="navigation-container"]/ul/li/a')
        for link in links:
            nombre = link.xpath(".//text()").get()
            link = link.xpath(".//@href").get()
            
            yield response.follow(url=link, callback=self.parse_productos)
            
    def parse_productos(self, response):
        
        for product in response.xpath("//ol[@class='products list items product-items  defer-images-grid']/li"):
            yield {
                
                'title': product.xpath(".//a[@class='product-item-link']/text()").get(),
                'price': product.xpath('.//span[@class="special-price"]//span[@class="price"]/text()').get()
                
            }
        
        next_page = response.xpath('//a[@class="action  next"]/@href').get()
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_productos)
        # productos = response.xpath('//a[@class="product-item-link"]/text()').getall()
        # precios = response.xpath('//span[@class="special-price"]//span[@class="price"]/text()').getall()

        # productos = [prod.strip() for prod in productos]

        # yield {
            
        #     'productos': productos,
        #     'precios': precios,
        #     'cant_registros': len(productos)
            
        #     }