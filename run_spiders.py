from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
from nltk.corpus import stopwords
from nltk import word_tokenize
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


    def stop_words(self):
        if self.tipo_busqueda in ['2', '3']:
            stop_words = frozenset(stopwords.words('spanish'))
            word_tokens = word_tokenize(self.target.lower())
            tokens = [w for w in word_tokens if not w in stop_words]
            return tokens
        else:
            return self.target.lower()

    def spiders_run(self):
        target_stop_words = self.stop_words()

        results = []
        process = CrawlerProcess(get_project_settings())
        
        if self.spiders_to_run == '5':
            self.spiders_to_run = self.paginas_hab.keys()

        for market in self.spiders_to_run:
            if market == '2':
               process.crawl(MusimundoSpider, target = target_stop_words, tipo_busqueda = self.tipo_busqueda )
            elif market == '4':
                process.crawl(CasaDelAudioSpider, target = target_stop_words, tipo_busqueda = self.tipo_busqueda )
            elif market == '1':
                process.crawl(CetrogarSpiderSpider, target = target_stop_words, tipo_busqueda = self.tipo_busqueda )
            elif market == '3':
                process.crawl(FravegaSpiderSpider, target = target_stop_words, tipo_busqueda = self.tipo_busqueda )
        
        def crawler_results(signal, sender, item, response, spider):
            results.append(item)
            
        dispatcher.connect(crawler_results, signal=signals.item_passed)
        process.start()
        return results
