# -*- coding: utf-8 -*-
import os
from sys import platform
from config import Config
from run_spiders import RunSpiders
from procesador import Procesador

class QuiereSalirException(Exception):
    pass

class Menu:

    def __init__(self):
        config = Config()
        self.__salir = False
        self.__target = ''
        self.__so = 'Unknown'
        self.__formato_out = '-1'

        self.__formatos_admitidos = config.get_formatos_admitidos()
        self.__paginas = config.get_paginas()
        self.__extras = config.get_extras()
        self.__tipos = config.get_tipos()
        
    def ejecutar(self):

        self.__limpiar_linea_de_comandos()
        try:
            while not self.__salir:
                self.__bienvenida()
                opcion = input("Ingrese el término de búsqueda >> ")

                if opcion == '1':
                    raise QuiereSalirException
                else:
                    self.__target = opcion.lower()
                    self.__paginas_elegidas = self.__pedir_pagina()
                    if len(self.__target.split(' ')) > 1:
                        self.__tipo = self.__tipo_busqueda()
                    else:
                        self.__tipo = '3'
                    # Ejecuto la busqueda ----------------
                    self.__buscar()
                    # ------------------------------------
                    self.__formato_out = self.__exportar()
                    # Se exporta a archivos ----------------
                    self.__exportar_a_archivos()
                    # --------------------------------------
                    self.__tabla_o_estadisticas = self.__pedir_extras()
                    # Se imprime tabla o estadística -----
                    self.__imprimir_tabla_o_estadistica()
                    # ------------------------------------
                    self.__salir = True
                    self.__despedirse()
        except QuiereSalirException:
            print('Saliendo...')
            self.__despedirse()
        except KeyboardInterrupt:
            print('Abortando...')

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
                raise QuiereSalirException
            else:
                print('Exportando: ...')
                print(f'Tipo: {self.__formatos_admitidos[self.__formato_out]}')
                return formato
        elif exportar == 'n':
            return exportar

    def __pedir_formato(self):
        formato = '-1'
        while formato not in self.__formatos_admitidos.keys():
            print('Elija el formato: \n')
            for k, v in self.__formatos_admitidos.items():
                print(f'{k}. {v} \n')
            print('0. Cancelar y salir \n')
            formato = input('>> ')
            if formato == '0':
                raise QuiereSalirException
            if formato not in self.__formatos_admitidos.keys():
                formato = '-1'
                print('Ingrese una opción válida... ')

        self.__formato_out = formato
        return formato

    def __pedir_pagina(self):
        pagina = '-1'
        while pagina not in self.__paginas.keys():
            print('\nElija la/s páginas de búsqueda.',
                  'Si son varias, separadas por coma: (Ej. 1,2,3) \n')
            for k, v in self.__paginas.items():
                print(f'{k}. {v} \n')
            print('0. Cancelar y salir \n')
            pagina = input('>> ')
            if pagina == '0':
                raise QuiereSalirException
            else:
                paginas_elegidas = pagina.split(',')
                flag_ok = True
                for elemento in paginas_elegidas:
                    if elemento not in self.__paginas.keys():
                        print('Elección inválida.')
                        pagina = '-1'
                        flag_ok = False
                if '5' in paginas_elegidas:
                    paginas_elegidas = '5'
                if flag_ok:
                    return paginas_elegidas

    def __tipo_busqueda(self):
        tipo = '-1'
        while tipo not in self.__tipos.keys():
            print('\nElija el tipo de búsqueda. \n')
            for k, v in self.__tipos.items():
                print(f'{k}. {v} \n')
            print('0. Cancelar y salir \n')
            tipo = input('>> ')
            if tipo == '0':
                raise QuiereSalirException
            if tipo not in self.__tipos.keys():
                tipo = '-1'
                print('Ingrese una opción válida... ')
            else:
                return tipo

    def __pedir_extras(self):
        extra = '-1'
        while extra not in self.__extras.keys():
            print('\n¿Desea obtener una estadística o tabla comparativa?. \n')
            for k, v in self.__extras.items():
                print(f'{k}. {v} \n')
            print('0. No. Finalizar. \n')
            extra = input('>> ')
            if extra == '0':
                raise QuiereSalirException
            if extra not in self.__extras.keys():
                extra = '-1'
                print('Ingrese una opción válida... ')
            else:
                return extra
    
    def __buscar(self):
        print(f'Buscando: {self.__target}')
        print(f'Tipo: {self.__tipos[self.__tipo]}')
        print('En: \n')
        for pagina in self.__paginas_elegidas:
            print(self.__paginas[pagina])
        
        run = RunSpiders( self.__paginas_elegidas  ,self.__target, self.__tipo)
        resultados = run.spiders_run()
        
        self.procesador = Procesador(resultados, self.__target.replace(' ','_')  )
    
    def __exportar_a_archivos(self):
        self.procesador.imprimirArchivo(self.__formatos_admitidos[self.__formato_out])
    
    def __imprimir_tabla_o_estadistica(self):
        self.procesador.tablaComparativa( self.__tabla_o_estadisticas )

    def get_target(self):
        return self.__target

    def get_so(self):
        return self.__so
