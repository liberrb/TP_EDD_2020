import scrapy

#para correrlo uso el comando scrapy runspider musimundo_spider.py -O output.json

class MusimundoSpider(scrapy.Spider):
    name = 'musimundo_spider'
    allowed_domain = ['www.musimundo.com']
    start_urls = ['https://www.musimundo.com/']

    def parse(self, response):
        links = response.xpath('//div[@class="navigationbarcollectioncomponent"]/div[@class="container"]/ul[@class="mus-navUl clear_fix"]/li/div/ul/li/div/div/h2/a')
        for link in links:
            link = link.xpath(".//@href").get()
            
            yield response.follow(url=link, callback=self.parse_productos)

    def parse_productos(self, response):
        for product in response.xpath('//div[@class="productGrid clearfix"]/div/div/div/a'):
            
            moneda = product.xpath('.//div[@class="mus-pro-quotes"]/div/span[@class="mus-pro-quotes-currency strong"]/text()').get()
            entero = product.xpath('.//div[@class="mus-pro-quotes"]/div/span[@class="mus-pro-quotes-price strong"]/text()').get()
            decimal = product.xpath('.//div[@class="mus-pro-quotes"]/div/span[@class="mus-pro-quotes-decimals strong"]/text()').get()

            yield {
                'title': product.xpath('normalize-space(.//div[@class="mus-pro-desc"]/p[@class="mus-pro-name"]/text())').get(),
                'price': moneda + entero + decimal
                #'price': product.xpath('.//div[@class="price-box-holder"]/div[@class="mus-pro-price-box"]/p[@class="mus-pro-price-cash"]/span[@class="line-trought strong"]/text()').get()
            }

        next_page = response.xpath('//li[@class="next square not-border"]/a/@href').get()
        if next_page:
            next_page = 'https://www.musimundo.com'+next_page
            yield scrapy.Request(url=next_page, callback=self.parse_productos)
