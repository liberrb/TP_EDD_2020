import Decoder
import csv
import datetime
import enum
import jsonpickle
import pandas 
import json
from json import JSONEncoder

class TiposArchivos(enum.Enum):
   csv = 1
   json = 2
   HTML = 3


class Procesador:

    def __init__(self,lista,criterio):
        lista.sort(key=lambda x: x.get('price'))
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
                    writer.writerow([item.get('title'), item.get('categoria'),"$ " + item.get('price'),item.get('link'),item.get('fecha')])
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
                html_str +="""<td>"""   + item.get('title') + """</td>"""
                html_str +="""<td>"""   + item.get('categoria') + """</td>"""
                html_str +="""<td>"""   + str(item.get('price')) + """</td>"""
                html_str +="""<td>"""   + item.get('link') + """</td>"""
                html_str +="""<td>"""   + item.get('fecha') + """</td>"""
                html_str +="""</tr>"""

            html_str +="""    </indent></table>"""
            Html_file= open(filename,"w")
            Html_file.write(html_str)
            Html_file.close()

    def contarElementosLista(self,lista):
        return {i:lista.count(i.get('title')) for i in lista}

    def tablaComparativa(self,tipo,modelo =""):
        resultado = []


        if(tipo == "a"):
            for item in self._miLista:
                if(modelo in item.get('title')):
                    resultado.append(item)
            resultado.sort(key=lambda x: x.get('price'))
        elif(tipo == "b"):
            elementos = self._miLista.groupby(['title']).mean()
            resultado = elementos
        else:
            elementos = self.contarElementosLista(self._miLista)
            for k, v in elementos.items():
                if(v == 1):
                    resultado.append(k)                    
        return resultado

    def estadisticas(self,tipo):
            tienda1 = []
            tienda2 = []
            tienda3 = []
            tienda4 = []
            for item in self._miLista:
                if(item.get('market') == 'casadelaudio'):
                    tienda1.append(item)
                elif(item.get('market') == 'musimundo'):
                    tienda2.append(item)
                elif(item.get('market') == 'fravega'):
                    tienda3.append(item) 
                else:
                    tienda4.append(item)