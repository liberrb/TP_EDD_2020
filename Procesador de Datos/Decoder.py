import json
from json import JSONEncoder
class items:
    def __init__(self, dict):
        vars(self).update( dict )


class itemsEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

class itemsDecoder:
        def decorder(self,jsonData):
            item = json.loads( jsonData, object_hook= items)
            return item


data='[{"title": "BOLSO MATERO NORTHLAND CITY BAG", "categoria": "M\u00c1S CATEGOR\u00cdAS", "price": "$ 4.608,00", "link": "https://www.musimundo.com/ms-categoras/bolsos-y-valijas/bolso-matero-northland-city-bag/p/00307151", "fecha": "07/11/2020 19:14:55"},{"title": "BOLSO MATERO NORTHLAND CITY BAG", "categoria": "M\u00c1S CATEGOR\u00cdAS", "price": "$ 4.608,00", "link": "https://www.musimundo.com/ms-categoras/bolsos-y-valijas/bolso-matero-northland-city-bag/p/00307150", "fecha": "07/11/2020 19:14:55"}]'
decoder = itemsDecoder()
itemJson = decoder.decorder(data)
print(itemJson[0].title)
