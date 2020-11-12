from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.musimundo_spider import MusimundoSpider
from spiders.casa_audio_spider import CasaDelAudioSpider
from spiders.cetrogar_spider import CetrogarSpiderSpider
from spiders.fravega_spider import FravegaSpiderSpider
from spiders.rodo_dos_spider import RodoDosSpiderSpider

from scrapy.signalmanager import dispatcher


def spider_musimundo_results(target, tipo_busqueda):
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)
        
    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(MusimundoSpider, target = target, tipo_busqueda = tipo_busqueda )
    process.start()
    return results

def spider_casa_audio_results(target, tipo_busqueda):
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)
        
    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(CasaDelAudioSpider, target = target, tipo_busqueda = tipo_busqueda )
    process.start()
    return results

def spider_cetrogar_results(target, tipo_busqueda):
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)
        
    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(CetrogarSpiderSpider, target = target, tipo_busqueda = tipo_busqueda )
    process.start()
    return results

def spider_fravega_results(target, tipo_busqueda):
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)
        
    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(FravegaSpiderSpider, target = target, tipo_busqueda = tipo_busqueda )
    process.start()
    return results

def spider_rodo_results(target, tipo_busqueda):
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)
        
    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(RodoDosSpiderSpider, target = target, tipo_busqueda = tipo_busqueda )
    process.start()
    return results





