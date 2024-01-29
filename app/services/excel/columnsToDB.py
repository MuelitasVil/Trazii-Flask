class fincas:
    Items = {
        '*Nombre' : 'FINA',
        '*Tipo de Sistema Ganadero' : 'FITE',
        '*Área' : 'FIAR',
        '*Unidad de Medida' : 'FIUM',
        '*Ubicación' :  'FIUB'
    }	

class potreros: 
    Items = {
        '*Identificación' : 'POTI',
        '*Área' : 'POTA',
        '*Unidad de Medida' : 'POUM',
        '*Tipo de Pasto' : 'POTT',
        'Georeferenciación' : 'POUB'
    }

class lotes:
    Items = {
        '*Nombre' : 'GACO',
        '*Tipo de Lote' : 'GATI'
    }

class bovino:
    Items = {
        '*Id' : 'BOID',
        'Id ICA' : 'BOCA',
        'Nombre' : 'BONO',
        '*Sexo' : 'BOSE',
        '*Raza' : 'BORA',
        'Color' : 'BOCO',
        'Marca' : 'BOMR', 
        'Fecha Nacimiento' : 'BOFN',
        'Fecha destete' : 'BOFD',
        'Peso al nacer kg' : 'BOPN',
        'Peso al destete kg' : 'BODE',
        'Fecha al destete' : 'BOFD',
        'Id Padre' : 'BOPA',
        'Nombre Padre' : 'BONP',
        'Raza Padre' : 'BORP',
        'Id Madre' : 'BOMA',
        'Nombre Madre' : 'BONM', 
        'Raza Madre' : 'BORM',
        'Estado Fisiologico' : 'BOES',
        'Estado reproductivo' : 'BORE',
        'Número de Partos' : 'BONN'
    }

ubicaciones = {
    'FIN' : [
            'POT',
            'GAN',
            'BOV'
        ]
    }

padres = {
        'POT' : 'FIN',
        'BOV' : 'GAN'
    }

class columnsTODB(object):
    fincas = fincas
    potreros = potreros
    bovinos = bovino
    lotes = lotes
    ubicaciones = ubicaciones
    padres = padres
