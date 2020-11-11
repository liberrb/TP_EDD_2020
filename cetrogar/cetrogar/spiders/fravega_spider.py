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
               
        for products in response.xpath("//ul[@class='listingDesktopstyled__SearchResultList-wzwlr8-6 fCKkuk']/li"):
            yield {
                'title': products.xpath(".//div/a/article/div/h4/text()[2]").get(),
                'price': products.xpath('.//div/a/article/div/div/span/text()').get()
            }
       
        next_page = response.xpath('//*[@id="__next"]/div[3]/div[2]/div/div/div[2]/section/ul[2]/ul/li[5]/a').get()
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_productos)   

