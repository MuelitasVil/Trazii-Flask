from app.services.sync.trazables.request import getRequestTrazable
from app.shared.localStorage import localStorage
from app.shared.constantsAPI import Config
from app.shared.trazables import Information_Trazables

def getDatos():

    url = Config.EndPoints.SINCRONIZACION_DATOS
    request = getRequestTrazable(url)
    
    Data = request['data']
    Length = request['count']

    storage = localStorage()
    Trazables = Information_Trazables()

    Cantidades =  Config.GlobalVars.Cantidades.copy()
    getData(Data, Trazables, Cantidades)

    storage.set_trazables(Trazables)
    storage.set_Cantidades(Cantidades)


def getData(data, Trazables, Cantidades):

    '''
    Se recorre cada dato retornado por la peticion, se verifica su tipo de
    trazable. Con el tipo de trazable se identifica en que diccionario va 
    a ser guardadada la informacion.

    Los diccionarios estan guardados en el objeto de Informacion_Trazables.
    '''
        
    for itemData in data:
        if itemData['trazable'] == Config.Trazables.BOVINO:
            Information_Bovinos = Trazables.Information_Bovinos
            setItemTrazable(Information_Bovinos, itemData, Cantidades)
        
        elif itemData['trazable'] == Config.Trazables.POTRERO:
            Information_Potreros = Trazables.Information_Potreros 
            setItemTrazable(Information_Potreros, itemData, Cantidades)
        
        elif itemData['trazable'] == Config.Trazables.FINCA:
            Information_Fincas = Trazables.Information_Fincas 
            setItemTrazable(Information_Fincas, itemData, Cantidades)
            
        elif itemData['trazable'] == Config.Trazables.COLABORADOR:
            Information_Colaboradores = Trazables.Information_Colaboradores 
            setItemTrazable(Information_Colaboradores, itemData, Cantidades)

        elif itemData['trazable'] == Config.Trazables.GANADO:
            Information_Ganado = Trazables.Information_Ganado
            setItemTrazable(Information_Ganado, itemData, Cantidades)
        
        elif itemData['trazable'] == Config.Trazables.PROPIETARIO:
            Information_Propietarios = Trazables.Information_Propietarios 
            setItemTrazable(Information_Propietarios, itemData, Cantidades)
        else:
            print(itemData['trazable'])

def setItemTrazable(Information_Trazable, itemData, Cantidades):

    '''
    En el diccionario que pertenece el trazable se guarda como llave primaria
    el trazii_id del trazable, el valor asociado a este trazable va a ser otro
    diccionario en el cual se va almacenar los items del trazable. 
    '''

    key = itemData['inventario']
    item = itemData['item']
    valor = itemData['valor']

    if key not in Information_Trazable:
        tipoTrazable = itemData['trazable']
        Information_Trazable[key] = {}
        Information_Trazable[key]['trazable'] = tipoTrazable
        Cantidades["Cant_" + tipoTrazable] += 1
        
    Information_Trazable[key][item] = valor

    