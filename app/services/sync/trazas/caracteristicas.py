import requests
from app.shared.constantsAPI import Config
from app.shared.localStorage import localStorage
from app.shared.trazas import Information_Trazas

def getCaracteristicas():

    '''
    Se extrae la informacion de las caracteristicas en un objeto de trazas
    para ser guardada en el localStorage
    '''
    
    storage = localStorage()
    
    subject_data = storage.get_subject_data()
    token = storage.get_token()

    params = {
        "inquilino" : subject_data["inquilino"],
        'desde' : '2023-11-26T20:10:18'
    }

    headers = {
        'Authorization': "{} {}".format(Config.GlobalVars.TYPE_OF_TOKEN, token),
        'agronegocio' : Config.GlobalVars.AGRONEGOCIO_BOVINO
    }

    request = requests.post(
        Config.EndPoints.SINCRONIZACION_CARACTERISICAS,
        params = params,
        json = [],
        headers = headers).json()
    
    Data = request['data']
    Length = request['count']
    trazas = storage.get_Trazas()

    getData(Data, trazas)

    storage.set_Ordeño(trazas.Information_Ordeño)
    storage.set_Pesaje(trazas.Information_Pesaje)
    storage.set_Servicio(trazas.Information_Servicio)
    storage.set_Palpacion(trazas.Information_Palpacion)
    storage.set_Parto(trazas.Information_Parto)
    storage.set_Compra(trazas.Information_Compra)

def getData(data, Trazas):
    
    '''
    Recorre la informacion de la sincrozacion de la peticion se compruebra el
    tipo de tarea y se guarda en su diccionario correspondiente ubicado en la
    clase trazas
    '''

    for tareaData in data:
        if tareaData['tarea'] == Config.Trazas.ORDEÑO:
            Information_Ordeño = Trazas.Information_Ordeño
            setCaracteristica(Information_Ordeño, tareaData)
        
        elif tareaData['tarea'] == Config.Trazas.PESAJE:
            Information_Pesaje = Trazas.Information_Pesaje 
            setCaracteristica(Information_Pesaje, tareaData)
        
        elif tareaData['tarea'] == Config.Trazas.SERVICIO:
            Information_Servicio = Trazas.Information_Servicio
            setCaracteristica(Information_Servicio, tareaData)
            
        elif tareaData['tarea'] == Config.Trazas.PALPACION:
            Information_Palpacion = Trazas.Information_Palpacion
            setCaracteristica(Information_Palpacion, tareaData)

        elif tareaData['tarea'] == Config.Trazas.PARTO:
            Information_Parto = Trazas.Information_Parto
            setCaracteristica(Information_Parto, tareaData)

        elif tareaData['tarea'] == Config.Trazas.COMPRA:
            Information_Compra = Trazas.Information_Compra
            setCaracteristica(Information_Compra, tareaData)
        else:
            tareaData['tarea']

def setCaracteristica(Information_Tarea, tareaData):
    inicio = tareaData['inicio']
    
    if inicio not in Information_Tarea:
        Information_Tarea[inicio] = {}

    if 'trazable' not in Information_Tarea[inicio]:
        Information_Tarea[inicio]['trazable'] = tareaData['trazable']     
    
    item = tareaData['item']
    valor = tareaData['valor']

    Information_Tarea[inicio][item] = valor
    