from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
from spiders.musimundo_spider import MusimundoSpider
from spiders.casa_audio_spider import CasaDelAudioSpider
from spiders.cetrogar_spider import CetrogarSpiderSpider
from spiders.fravega_spider import FravegaSpiderSpider
from config import Config



class RunSpiders():
    def __init__(self, spiders_to_run, target, tipo_busqueda):
        self.spiders_to_run = spiders_to_run
        self.target = target
        self.tipo_busqueda = tipo_busqueda
        self.paginas_hab = Config().get_paginas()

    def spiders_run(self):
        results = []
        process = CrawlerProcess(get_project_settings())
        
        if self.spiders_to_run == '5':
            self.spiders_to_run = self.paginas_hab.keys()

        for market in self.spiders_to_run:
            if market == '2':
               process.crawl(MusimundoSpider, target = self.target, tipo_busqueda = self.tipo_busqueda )
            elif market == '4':
                process.crawl(CasaDelAudioSpider, target = self.target, tipo_busqueda = self.tipo_busqueda )
            elif market == '1':
                process.crawl(CetrogarSpiderSpider, target = self.target, tipo_busqueda = self.tipo_busqueda )
            elif market == '3':
                process.crawl(FravegaSpiderSpider, target = self.target, tipo_busqueda = self.tipo_busqueda )
        
        def crawler_results(signal, sender, item, response, spider):
            results.append(item)
            
        dispatcher.connect(crawler_results, signal=signals.item_passed)
        process.start()
        return results
