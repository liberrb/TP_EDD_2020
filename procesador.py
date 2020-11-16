import decoder
import csv
import datetime
import enum
import jsonpickle
import json
from json import JSONEncoder
from config import Config
import os
import errno
from difflib import SequenceMatcher as SM
import difflib

class ItemsAuxiliar():
    def __init__(self,title,categoria,price,link,fecha,market,promedio,cantidad):
        self.title = title
        self.categoria = categoria
        self.price = price
        self.link = link
        self.fecha = fecha
        self.market = market
        self.promedio = promedio
        self.cantidad = cantidad


class Procesador:

    def __init__(self,lista,criterio):
        lista.sort(key=lambda x: x.get('price'))
        self._miLista = lista
        self._criterio = criterio


    def imprimirArchivo(self,tipoArchivos):

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

    def guardarTablaHtmlComparativa(self,lista,nombreItem):
       
        path = Config().get_path()

        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        nombreItem = nombreItem.replace("/","_")
        filename = path + nombreItem.replace(" ","_") +  "." + "html"

        html_str = ""
        if(nombreItem != "ComparativaOrdenada"):
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
            for item in lista:
                html_str +="""<tr>"""
                html_str +="""<td>"""   + str(item.get('title')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('categoria')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('price')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('link')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('fecha')) + """</td>"""
                html_str +="""</tr>"""
        else:
            html_str = """
            <table border=1>
                <tr>
                <th>Title</th>
                <th>Categoria</th>
                <th>Price</th>
                <th>Link</th>
                <th>Fecha</th>
                <th>Promedio</th>
                <th>Cantidad</th>
                </tr>
                <indent>""" 
            for item in lista:
                html_str +="""<tr>"""
                html_str +="""<td>"""   + str(item.title) + """</td>"""
                html_str +="""<td>"""   + str(item.categoria) + """</td>"""
                html_str +="""<td>"""   + str(item.price) + """</td>"""
                html_str +="""<td>"""   + str(item.link) + """</td>"""
                html_str +="""<td>"""   + str(item.fecha) + """</td>"""
                html_str +="""<td>"""   + str(item.promedio) + """</td>"""
                html_str +="""<td>"""   + str(item.cantidad) + """</td>"""
                html_str +="""</tr>"""
        
        html_str +="""    </indent></table>"""
        Html_file= open(filename,"w")
        Html_file.write(html_str)
        Html_file.close()

    def tablaComparativa(self,tipo,modelo =""):
        resultado = []
        resultadoYaestan = []
        if(tipo == '1'):
            for item in self._miLista:
                if(item.get('title') not in resultadoYaestan):
                    for producto in self._miLista:                   
                        if(item != producto and SM(None, item.get('title').lower(), producto.get('title').lower()).ratio() >= 0.6):
                            resultado.append(producto)
                            resultadoYaestan.append(producto.get('title'))
                    if(len(resultado) > 0):
                        resultado.append(item)
                        self.guardarTablaHtmlComparativa(resultado,item.get('title'))
                    resultado.clear()    
        elif(tipo == '2'):
            for item in self._miLista:
                if(item.get('title') not in resultadoYaestan):
                    suma = 0
                    for producto in self._miLista:                   
                        if(item != producto and SM(None, item.get('title').lower(), producto.get('title').lower()).ratio() >= 0.6):
                            suma += producto.get('price')
                            resultado.append(producto)
                            resultadoYaestan.append(producto.get('title'))
                    cantidadItems = len(resultado)
                    if(cantidadItems > 0):
                        suma += item.get('price')
                        aGuardar = ItemsAuxiliar(item.get('title'),item.get('categoria'),item.get('price'),item.get('link'),item.get('fecha'),item.get('market'),suma/cantidadItems,cantidadItems)
                        resultado.append(aGuardar)
            self.guardarTablaHtmlComparativa(resultado,"ComparativaOrdenada")
            resultado.clear()    
        else:
            for item in self._miLista:
                for producto in self._miLista:                   
                    if(item != producto and SM(None, item.get('title').lower(), producto.get('title').lower()).ratio() >= 0.6):
                        resultado.append(producto)
                    if(len(resultado) == 0):
                        resultado.append(item)
            self.guardarTablaHtmlComparativa(resultado,"Unicos")                   

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





s1 = 'Celular Libre Samsung Galaxy S20 Ultra Gris'
s2 = 'CELULAR LIBRE SAMSUNG S20 ULTRA GRIS'
print(SM(None, s1.lower(), s2.lower()).ratio())


lista1 = ["Celular Libre Samsung Galaxy S20 Ultra Gris"]
lista2 = ["Celular Libre Samsung S20 6.2 8/128 Gris",
          "CELULAR LIBRE SAMSUNG S20 ULTRA GRIS",
          "CELULAR SAMSUNG GALAXY S20+ GRIS",
          "CELULAR SAMSUNG GALAXY S20 AZUL",
          "Funda Samsung LED Back Cover S10 White",
          "Celular Libre Samsung S10 ",]

d = difflib.Differ()

for item in lista1:
    for producto in lista2:                   
        if(item != producto and SM(None, item.lower(), producto.lower()).ratio() >= 0.6):
            print(producto)