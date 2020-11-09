from spiders.musimundo_spider import MusimundoSpider


spider = MusimundoSpider(prod="COCHE")
a = spider
print(type(a))
print('imprimiendo spider')
for s in a:
    print(s)