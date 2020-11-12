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



