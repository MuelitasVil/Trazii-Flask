import requests
from app.shared.localStorage import localStorage
from app.shared.constantsAPI import Config
from app.shared.trazables import Information_Trazables

def getDatos():

    '''
    Se extrae la informacion de los datos en un objeto de trazables
    para ser guardada en el localStorage.

    Ademas se cuenta la cantidad de articulos que tiene un trazable
    '''

    storage = localStorage()
    token = storage.get_token()
    subject_data = storage.get_subject_data()

    params = {
        "inquilino" : subject_data["inquilino"],
    }

    headers = {
        'Authorization': "{} {}".format(Config.GlobalVars.TYPE_OF_TOKEN, token),
        'agronegocio' : Config.GlobalVars.AGRONEGOCIO_BOVINO
    }

    Cantidades =  Config.GlobalVars.Cantidades.copy()

    request = requests.post(
        Config.EndPoints.END_POINT_SINCRONIZACION_DATOS,
        params = params,
        json = [],
        headers = headers).json()
    
    Data = request['data']
    Length = request['count']

    Trazables = Information_Trazables()

    getData(Data, Trazables, Cantidades)

    storage.set_Bovinos(Trazables.Information_Bovinos) 
    storage.set_Colaboradores(Trazables.Information_Colaboradores)
    storage.set_Fincas(Trazables.Information_Fincas)
    storage.set_Ganado(Trazables.Information_Ganado)
    storage.set_Potreros(Trazables.Information_Potreros)
    storage.set_Propietarios(Trazables.Information_Propietarios)
    storage.set_Cantidades(Cantidades)

def getData(data, Trazables, Cantidades):
    for itemData in data:
        if itemData['trazable'] == Config.Trazables.BOVINO:
            Information_Bovinos = Trazables.Information_Bovinos
            setItemTrazable(Information_Bovinos, itemData)
            Cantidades['cantidadBovinos'] += 1 
        
        elif itemData['trazable'] == Config.Trazables.POTRERO:
            Information_Potreros = Trazables.Information_Potreros 
            setItemTrazable(Information_Potreros, itemData)
            Cantidades['cantidadPotreros'] += 1
        
        elif itemData['trazable'] == Config.Trazables.FINCA:
            Information_Fincas = Trazables.Information_Fincas 
            setItemTrazable(Information_Fincas, itemData)
            Cantidades['cantidadFincas'] += 1
            
        elif itemData['trazable'] == Config.Trazables.COLABORADOR:
            Information_Colaboradores = Trazables.Information_Colaboradores 
            setItemTrazable(Information_Colaboradores, itemData)
            Cantidades['cantidadGanado'] += 1  

        elif itemData['trazable'] == Config.Trazables.GANADO:
            Information_Ganado = Trazables.Information_Ganado
            setItemTrazable(Information_Ganado, itemData)
            Cantidades['cantidadColaboradores'] += 1
        
        elif itemData['trazable'] == Config.Trazables.PROPIETARIO:
            Information_Propietarios = Trazables.Information_Propietarios 
            setItemTrazable(Information_Propietarios, itemData)
            Cantidades['cantidadPropietarios'] += 1

        else:
            print(itemData['trazable'])


def setItemTrazable(Information_Trazable, itemData):
    key = itemData['inventario']
    item = itemData['item']
    valor = itemData['valor']

    if key not in Information_Trazable:
        Information_Trazable[key] = {}
        Information_Trazable[key]['trazable'] = itemData['trazable']
        
    Information_Trazable[key][item] = valor
