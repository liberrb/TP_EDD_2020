from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.musimundo_spider import MusimundoSpider

from scrapy.signalmanager import dispatcher


def spider_results():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)
        
    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(MusimundoSpider)
    process.start()
    return results


if __name__ == '__main__':
    a = spider_results()
    print(type(a))
    print(len(a))
    print('itero resultados')
    print(a[0])