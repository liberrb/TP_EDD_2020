import decoder
import csv
import datetime
import enum
import jsonpickle
#import pandas 
import json
from json import JSONEncoder
from config import Config
import os
import errno


class Procesador:

    def __init__(self,lista,criterio):
        lista.sort(key=lambda x: x.get('price'))
        self._miLista = lista
        self._criterio = criterio


    def ImprimirArchivo(self,tipoArchivos):

        path = Config().get_path()

        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        filename = path + self._criterio + "_" + datetime.datetime.now().strftime("%d-%m-%Y") + "." + tipoArchivos
        if tipoArchivos == 'csv':       
            with open(filename, 'w') as f:
                writer = csv.writer(f)
                writer = csv.writer(open(filename, 'w'), delimiter=';')
                headers = ['Title', 'Categoria', 'Price', 'Link', 'Fecha']
                writer.writerow(headers)
                for item in self._miLista:
                    writer.writerow([item.get('title'), str(item.get('categoria')),"$ " + str(item.get('price')) ,item.get('link'),str(item.get('fecha'))])
        elif tipoArchivos == 'json':
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
                html_str +="""<td>"""   + str(item.get('title')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('categoria')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('price')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('link')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('fecha')) + """</td>"""
                html_str +="""</tr>"""

            html_str +="""    </indent></table>"""
            Html_file= open(filename,"w")
            Html_file.write(html_str)
            Html_file.close()

    def contarElementosLista(self,lista):
        return {i:lista.count(i.get('title')) for i in lista}

    def TablaComparativa(self,tipo,modelo =""):
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

