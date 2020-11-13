from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
#from twisted.internet import reactor
from nltk.corpus import stopwords
from nltk import word_tokenize
from spiders.musimundo_spider import MusimundoSpider
from spiders.casa_audio_spider import CasaDelAudioSpider
from spiders.cetrogar_spider import CetrogarSpiderSpider
from spiders.fravega_spider import FravegaSpiderSpider
from spiders.rodo_dos_spider import RodoDosSpiderSpider


class RunSpiders():
    def __init__(self, spiders_to_run, target, tipo_busqueda):
        self.spiders_to_run = spiders_to_run
        self.target = target
        self.tipo_busqueda = tipo_busqueda

    def stop_words(self):
        if self.tipo_busqueda in [2 ,3]:
            stop_words = frozenset(stopwords.words('spanish'))
            word_tokens = word_tokenize(self.target.lower())
            tokens = [w for w in word_tokens if not w in stop_words]
            return tokens
        else:
            return self.target.lower()

    def spiders_run(self):

        target = self.stop_words()

        results = []
        process = CrawlerProcess(get_project_settings())
        for market in self.spiders_to_run:
            if market == 'musimundo':
               process.crawl(MusimundoSpider, target = target, tipo_busqueda = self.tipo_busqueda )
            elif market == 'casaAudio':
                process.crawl(CasaDelAudioSpider, target = target, tipo_busqueda = self.tipo_busqueda )
            elif market == 'cetrogar':
                process.crawl(CetrogarSpiderSpider, target = target, tipo_busqueda = self.tipo_busqueda )
            elif market == 'fravega':
                process.crawl(FravegaSpiderSpider, target = target, tipo_busqueda = self.tipo_busqueda )
            elif market == 'rodo':
                process.crawl(RodoDosSpiderSpider, target = target, tipo_busqueda = self.tipo_busqueda )
        
        def crawler_results(signal, sender, item, response, spider):
            results.append(item)
            
        dispatcher.connect(crawler_results, signal=signals.item_passed)
        process.start()
        return results
