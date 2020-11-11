import scrapy


class RodoDosSpiderSpider(scrapy.Spider):
    name = 'rodo_dos_spider'
    allowed_domains = ['www.rodo.com.ar']
    start_urls = ['https://www.rodo.com.ar/productos.html']

    def parse(self, response):
        links = response.xpath('//dd[@class="last odd current"]/ol/li/a')
        for link in links:
            nombre = link.xpath(".//text()").get()
            link = link.xpath(".//@href").get()
                
            yield response.follow(url=link, callback=self.parse_products)
                
    def parse_products(self, response):
                        
        for products in response.xpath("//ul[@class='products-grid products-grid--max-4-col first last odd']/li"):
            yield {
                'title': products.xpath(".//div/h2").get(),
                'price': products.xpath('.//div/div[@class="price-box"]/p/span[2]/text()').get()
            }

        next_page = response.xpath('//a[@class="next i-next"]/@href').get()
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_productos)