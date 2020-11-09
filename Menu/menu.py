# -*- coding: utf-8 -*-
import os
from sys import platform
import scrapy
from scrapy.crawler import CrawlerProcess
import re
from cetrogar_spider import CetrogarSpiderSpider

class Menu:
    
    def __init__(self):
        self.__salir = False
        self.__target = ''
        self.__so = 'Unknown'
        self.__formatos_admitidos = {'1': 'csv', '2': 'json', '3': 'csv y json'}
        self.__formato_out = '-1'
        
    def ejecutar(self):
    
        self.__limpiar_linea_de_comandos()
        
        while not self.__salir:
            
            self.__bienvenida()
            opcion = input("Ingrese el término de búsqueda >> ")
            
            if opcion == '1':
                self.__salir = True
                self.__despedirse()
            else:
                self.__target = opcion.lower()
                print(f'Buscando: {self.__target}')
                ##-------------- ejecuto la busqueda
                process = CrawlerProcess()
                process.crawl(CetrogarSpiderSpider, target=self.__target)
                process.start()
                ##--------------
                print(f'Tu búsqueda arrojó los siguientes resultados: ')
                print('...')
                self.__exportar()
        
    def __limpiar_linea_de_comandos(self):
        
        if platform == "linux" or platform == "linux2":
            # linux
            os.system('clear')
            self.__so = 'linux'
        elif platform == "darwin":
            # OS X
            os.system('clear')
            self.__so = 'mac'
        elif platform == "win32":
            # Windows...
            os.system('cls')
            self.__so = 'windows'
            
    def __despedirse(self):
        print('Fin del programa.')
        
    def __bienvenida(self):
        print('¡Hola! Ingresá el producto que deseás buscar o el número 1 para salir.')
        
    def __exportar(self):
        exportar = input('¿Desea exportar los resultados? [y/n] >> ')
        exportar = exportar.lower()
        while exportar not in ['y', 'n']:
            exportar = input('No entendí... ¿Desea exportar los resultados? [y/n] >> ')
            exportar = exportar.lower()
        if exportar == 'y':
            formato = self.__pedir_formato()
            if formato == '0':
                self.__salir = True
                self.__despedirse()
            else:
                print(f'Exportando: ...')
                print(f'Tipo: {self.__formatos_admitidos[self.__formato_out]}')
                self.__salir = True
                self.__despedirse()
        elif exportar == 'n':    
            self.__salir = True
            self.__despedirse()
            
    def __pedir_formato(self):
        formato = '-1'
        while formato not in ['1', '2', '3']:
            print('Elija el formato: \n')
            for k,v in self.__formatos_admitidos.items():
                print(f'{k}. {v} \n')
            print('0. Cancelar y salir \n')
            formato = input('>> ')
            if formato == '0':
                break
            if formato not in self.__formatos_admitidos.keys():
                formato = '-1'
                print('Ingrese una opción válida... ')

        self.__formato_out = formato
        return formato
        
    def get_target(self):
        return self.__target
    
    def get_so(self):
        return self.__so
    