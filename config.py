import pathlib

class Config():

    directorio_descarga = str(pathlib.Path().absolute()) + '/resultados/' 

    paginas = {
               '1': 'Cetrogar', 
               '2': 'Musimundo', 
               '3': 'Frávega', 
               '4': 'La Casa Del Audio', 
               '5': 'Todas'
               }

    formatos_admitidos = {
                          '1': 'csv', 
                          '2': 'json', 
                          '3': 'html'
                         }

    extras = {
              '1': 'Estadísticas por modelo',
              '2': 'Estadísticas por promedio',
              '3': 'Unicos por tienda',
              #'3': 'Tabla comparativa', 
              #'4': 'Ambas'
             }

    tipos = {
             '1': 'Frase exacta', 
             '2': 'Todas las palabras', 
             '3': 'Alguna de las palabras'
            }

    start_urls = {
                  'casa_del_audio' : 'https://www.casadelaudio.com/',
                  'cetrogar' : 'https://www.cetrogar.com.ar/',
                  'fravega' : 'https://www.fravega.com/',
                  'musimundo' : 'https://www.musimundo.com/'
                 }

    porcetanje_exactitud = 0.85
    porcetanje_exactitud_2 = 0.95

    def get_path(self):
        return self.directorio_descarga

    def get_paginas(self):
        return self.paginas

    def get_formatos_admitidos(self):
        return self.formatos_admitidos
    
    def get_extras(self):
        return self.extras

    def get_tipos(self):
        return self.tipos

    def get_start_url(self):
        return self.start_urls
    
    def get_exactitud(self):
        return self.porcetanje_exactitud
    
    def get_exactitud_2(self):
        return self.porcetanje_exactitud_2


