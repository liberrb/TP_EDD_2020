import Decoder
import csv
import datetime
import enum
import jsonpickle
import json
from json import JSONEncoder

class TiposArchivos(enum.Enum):
   csv = 1
   json = 2
   HTML = 3


class Procesador:

    def __init__(self,lista,criterio):
        lista.sort(key=lambda x: x.price)
        self._miLista = lista
        self._criterio = criterio


    def ImprimirArchivo(self,tipoArchivos):
        filename = self._criterio + "_" + datetime.datetime.now().strftime("%d-%m-%Y") + "." + tipoArchivos.name
        if tipoArchivos == TiposArchivos.csv:          
            with open(filename, 'w') as f:
                writer = csv.writer(f)
                writer = csv.writer(open(filename, 'w'), delimiter=';')
                headers = ['Title', 'Categoria', 'Price', 'Link', 'Fecha']
                writer.writerow(headers)
                for item in self._miLista:
                    writer.writerow([item.title, item.categoria,"$ " + item.price,item.link,item.fecha])
        elif tipoArchivos == TiposArchivos.json:
            jsonString = jsonpickle.encode(self._miLista, unpicklable=False)
            with open(filename, 'w') as f:
                json.dump(jsonString, f)
        else:
            html_str = """
            <table border=1>
                <tr>
                <th>Title</th>
                <th>Categoria</th>
                <th>Price</th>
                <th>Link</th>
                <th>Fecha</th>
                </tr>
                <indent>""" 

            for item in self._miLista:
                html_str +="""<tr>"""
                html_str +="""<td>"""   + item.title + """</td>"""
                html_str +="""<td>"""   + item.categoria + """</td>"""
                html_str +="""<td>"""   + item.price + """</td>"""
                html_str +="""<td>"""   + item.link + """</td>"""
                html_str +="""<td>"""   + item.fecha + """</td>"""
                html_str +="""</tr>"""

            html_str +="""    </indent></table>"""
            Html_file= open(filename,"w")
            Html_file.write(html_str)
            Html_file.close()


data='[{"title": "BOLSO MATERO NORTHLAND CITY BAG", "categoria": "M\u00c1S CATEGOR\u00cdAS", "price": "4610,10", "link": "https://www.musimundo.com/ms-categoras/bolsos-y-valijas/bolso-matero-northland-city-bag/p/00307151", "fecha": "07/11/2020 19:14:55"},{"title": "BOLSO MATERO NORTHLAND CITY BAG", "categoria": "M\u00c1S CATEGOR\u00cdAS", "price": "4608,02", "link": "https://www.musimundo.com/ms-categoras/bolsos-y-valijas/bolso-matero-northland-city-bag/p/00307150", "fecha": "07/11/2020 19:14:55"}]'
decoder = Decoder.itemsDecoder()
itemJson = decoder.decorder(data)
miProcesador = Procesador(itemJson,"Bolsos")
miProcesador.ImprimirArchivo(TiposArchivos.HTML)
