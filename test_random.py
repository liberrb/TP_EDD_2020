from utils import Utils
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