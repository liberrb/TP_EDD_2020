
class Config():

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
                          '3': 'html', 
                          '4': 'Todos'
                         }

    extras = {
              '1': 'Estadísticas', 
              '2': 'Tabla comparativa', 
              '3': 'Ambas'
             }

    tipos = {
             '1': 'Frase exacta', 
             '2': 'Todas las palabras', 
             '3': 'Alguna de las palabras'
            }

    start_urls = {
                  'casa_del_audio' : 'https://www.casadelaudio.com/',
                  'cetrogar' : '',
                  'gravega' : '',
                  'musimundo' : ''

                 }

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


