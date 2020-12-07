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
    def __init__(self,title,categoria,price,fecha,promedio,cantidad):
        self.title = title
        self.categoria = categoria
        self.price = price
        self.fecha = fecha
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

        if (nombreItem == "Unicos"):
            html_str = """
            <table border=1>
                <tr>
                <th>Title</th>
                <th>Categoria</th>
                <th>Price</th>
                <th>market</th>
                <th>Fecha</th>
                </tr>
                <indent>""" 
            for item in lista:
                html_str +="""<tr>"""
                html_str +="""<td>"""   + str(item.get('title')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('categoria')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('price')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('market')) + """</td>"""
                html_str +="""<td>"""   + str(item.get('fecha')) + """</td>"""
                html_str +="""</tr>"""
        elif(nombreItem != "ComparativaOrdenada"):
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
                html_str +="""<td>"""   + str(item.fecha) + """</td>"""
                html_str +="""<td>"""   + str(item.promedio) + """</td>"""
                html_str +="""<td>"""   + str(item.cantidad) + """</td>"""
                html_str +="""</tr>"""
        
        html_str +="""    </indent></table>"""
        Html_file= open(filename,"w")
        Html_file.write(html_str)
        Html_file.close()

    def tablaComparativa(self,tipo,modelo =""):
        config = Config()
        resultado = []
        resultadoYaestan = []
        if(tipo == '1'):
            for item in self._miLista:
                if(item.get('title') not in resultadoYaestan):
                    for producto in self._miLista:                   
                        if(item != producto and SM(None, item.get('title').lower(), producto.get('title').lower()).ratio() >= config.get_exactitud() ):
                            resultado.append(producto)
                            resultadoYaestan.append(producto.get('title'))
                    if(len(resultado) > 0):
                        resultado.append(item)
                        self.guardarTablaHtmlComparativa(resultado,item.get('title'))
                    resultado.clear()    
        elif(tipo == '2'):
            lista_aux = []
            for item in self._miLista:
                suma = 0
                cantidadItems = 0
                if item.get('price') != 0:
                    if(item.get('title') not in resultadoYaestan):
                        for producto in self._miLista:
                            if(item != producto and SM(None, item.get('title').lower(), producto.get('title').lower()).ratio() >= config.get_exactitud_2() ):
                                suma += producto.get('price')
                                resultado.append(producto)
                                resultadoYaestan.append(producto.get('title'))
                        cantidadItems = len(resultado)
                        if(cantidadItems > 0):
                            cantidadItems += 1
                            suma += item.get('price')
                            aGuardar = ItemsAuxiliar(item.get('title'),item.get('categoria'),item.get('price'),item.get('fecha'),suma/cantidadItems,cantidadItems)
                            lista_aux.append(aGuardar)
                resultado.clear()
            self.guardarTablaHtmlComparativa(lista_aux,"ComparativaOrdenada")
            lista_aux.clear() 
              
        else:
            resultado_aux = []
            for item in self._miLista:
                for producto in self._miLista:                   
                    if(item != producto and SM(None, item.get('title').lower(), producto.get('title').lower()).ratio() >= config.get_exactitud() ):
                        resultado_aux.append(producto)
                if(len(resultado_aux) == 0):
                    resultado.append(item)
                resultado_aux.clear()
            self.guardarTablaHtmlComparativa(resultado,"Unicos")                   