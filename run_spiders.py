from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from spiders.musimundo_spider import MusimundoSpider
from spiders.casa_audio_spider import CasaDelAudioSpider
from spiders.cetrogar_spider import CetrogarSpiderSpider
from spiders.fravega_spider import FravegaSpiderSpider
from spiders.rodo_dos_spider import RodoDosSpiderSpider

from scrapy.signalmanager import dispatcher

class RunSpiders():
    def __init__(self, spiders_to_run, target, tipo_busqueda):
        self.spiders_to_run = spiders_to_run
        self.target = target #tengo que meter las stop words segun el tipo de busqueda
        self.tipo_busqueda = tipo_busqueda

    def spiders_run(self):
        results = []
        process = CrawlerProcess(get_project_settings())
        for market in self.spiders_to_run:
            if market == 'musimundo':
               process.crawl(MusimundoSpider, target = self.target, tipo_busqueda = self.tipo_busqueda )
            elif market == 'casaAudio':
                process.crawl(CasaDelAudioSpider, target = self.target, tipo_busqueda = self.tipo_busqueda )
            elif market == 'cetrogar':
                process.crawl(CetrogarSpiderSpider, target = target, tipo_busqueda = tipo_busqueda )
            elif market == 'fravega':
                process.crawl(FravegaSpiderSpider, target = target, tipo_busqueda = tipo_busqueda )
            elif market == 'rodo':
                process.crawl(RodoDosSpiderSpider, target = target, tipo_busqueda = tipo_busqueda )
        
        def crawler_results(signal, sender, item, response, spider):
            results.append(item)
            
        dispatcher.connect(crawler_results, signal=signals.item_passed)
        process.start()
        return results

    # def spider_musimundo_results(self, target, tipo_busqueda):
    #     results = []

    #     def crawler_results(signal, sender, item, response, spider):
    #         results.append(item)
            
    #     dispatcher.connect(crawler_results, signal=signals.item_passed)

    #     process = CrawlerProcess(get_project_settings())
    #     process.crawl(MusimundoSpider, target = target, tipo_busqueda = tipo_busqueda )
    #     process.start()
    #     return results

    # def spider_casa_audio_results(self, target, tipo_busqueda):
    #     results = []

    #     def crawler_results(signal, sender, item, response, spider):
    #         results.append(item)
            
    #     dispatcher.connect(crawler_results, signal=signals.item_passed)

    #     process = CrawlerProcess(get_project_settings())
    #     process.crawl(CasaDelAudioSpider, target = target, tipo_busqueda = tipo_busqueda )
    #     process.start()
    #     return results

    # def spider_cetrogar_results(self, target, tipo_busqueda):
    #     results = []

    #     def crawler_results(signal, sender, item, response, spider):
    #         results.append(item)
            
    #     dispatcher.connect(crawler_results, signal=signals.item_passed)

    #     process = CrawlerProcess(get_project_settings())
    #     process.crawl(CetrogarSpiderSpider, target = target, tipo_busqueda = tipo_busqueda )
    #     process.start()
    #     return results

    # def spider_fravega_results(self, target, tipo_busqueda):
    #     results = []

    #     def crawler_results(signal, sender, item, response, spider):
    #         results.append(item)
            
    #     dispatcher.connect(crawler_results, signal=signals.item_passed)

    #     process = CrawlerProcess(get_project_settings())
    #     process.crawl(FravegaSpiderSpider, target = target, tipo_busqueda = tipo_busqueda )
    #     process.start()
    #     return results

    # def spider_rodo_results(self, target, tipo_busqueda):
    #     results = []

    #     def crawler_results(signal, sender, item, response, spider):
    #         results.append(item)
            
    #     dispatcher.connect(crawler_results, signal=signals.item_passed)

    #     process = CrawlerProcess(get_project_settings())
    #     process.crawl(RodoDosSpiderSpider, target = target, tipo_busqueda = tipo_busqueda )
    #     process.start()
    #     return results

