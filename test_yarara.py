from utils import Utils
from procesador import Procesador
from os import path
import pathlib
import datetime
from config import Config

utils = Utils()
def test_tipo_busqueda_1():
    '''Publicación con la frase exacta'''
    target = 'Lavarropas Carga Frontal Longvie 8 Kg 1200 RPM L18012'
    title = 'Lavarropas Carga Frontal Longvie 8 Kg 1200 RPM L18012'
    assert utils.tipo_busqueda_1(target, title)

def test_tipo_busqueda_2():
    '''Publicación que contenga todas las palabras'''
    target = 'Lavarropas Carga Frontal Longvie 8 Kg 1200 RPM L18012'
    title = 'Lavarropas Carga Frontal Longvie 8 Kg 1200 RPM L18012'
    assert utils.tipo_busqueda_2(target, title)

def test_tipo_busqueda_3():
    '''Publicación que contenga algunas de las palabras.'''
    target = 'Lavarropas Longvie'
    title = 'Lavarropas Carga Frontal Longvie 8 Kg 1200 RPM L18012'
    assert utils.tipo_busqueda_3(target, title)

#fragmeto extraido de un scrapeo donde criterio fue longvie, pero para lo cambio a restados_test para test
lista = [{'categoria': 'Electrodomésticos','fecha': '15/11/2020 12:26:02',
 'link': 'https://www.cetrogar.com.ar/aspiradora-electrolux-gt30n-1300w.html',
 'market': 'cetrogar', 'price': 12109.0,
 'title': 'Calefactor Longvie EC3200ECA3 Con Multigas'}, {'categoria': 'Electrodomésticos',
 'fecha': '15/11/2020 12:26:07',
 'link': 'https://www.cetrogar.com.ar/aspiradora-yelmo-as-3228-2000w-sin-bolsa.html',
 'market': 'cetrogar', 'price': 23899.0,
 'title': 'Termotanque Longvie Electrico para colgar TE40F Carga Inferior'}, {'categoria': 'Electrodomésticos',
 'fecha': '15/11/2020 12:26:07',
 'link': 'https://www.cetrogar.com.ar/cafetera-nespressor-inissia-red-aeroccino-3-a3c40-ar-re-ne.html',
 'market': 'cetrogar', 'price': 29999.0,
 'title': 'Termotanque Longvie Multigas Colgar 50 Litros inferior'}, {'categoria': 'Electrodomésticos',
 'fecha': '15/11/2020 12:26:08',
 'link': 'https://www.cetrogar.com.ar/microondas-bgh-qchef-28l-b228db-bl.html',
 'market': 'cetrogar', 'price': 43799.0,
 'title': 'Lavarropas Longvie L16508 6.5Kg 800rpm'}, {'categoria': 'Electrodomésticos',
 'fecha': '15/11/2020 12:26:08',
 'link': 'https://www.cetrogar.com.ar/anafe-longvie-a-6600g-x-4-hornallas-gas.html',
 'market': 'cetrogar', 'price': 48999.0, 'title': 'Anafe Longvie A-6600G x 4 Hornallas Gas'}]

criterio = 'resultados test'.replace(' ','_')
procesador = Procesador(lista, criterio)

def test_imprimir_archivo_csv():
    procesador.ImprimirArchivo('csv')
    filename = criterio + "_" + datetime.datetime.now().strftime("%d-%m-%Y") + '.csv'
    assert path.isfile('resultados/' + filename)

def test_imprimir_archivo_json():
    procesador.ImprimirArchivo('json')
    filename = criterio + "_" + datetime.datetime.now().strftime("%d-%m-%Y") + '.json'
    assert path.isfile('resultados/' + filename)

def test_imprimir_archivo_html():
    procesador.ImprimirArchivo('html')
    filename = criterio + "_" + datetime.datetime.now().strftime("%d-%m-%Y") + '.html'
    assert path.isfile('resultados/' + filename)

config = Config()
def test_config_paginas():
    assert config.get_paginas()['5'] == 'Todas'

def test_config_formatos_admitidos():
    assert config.get_formatos_admitidos()['2'] == 'json'

def test_config_tipos():
    assert config.get_tipos()['3'] == 'Alguna de las palabras'

def test_config_url():
    assert config.get_start_url()['fravega'] == 'https://www.fravega.com/'
