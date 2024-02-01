from app.services.sync.trazables.request import getRequestTrazable
from app.shared.constantsAPI import Config
from app.shared.localStorage import localStorage
from app.shared.trazables import Information_Trazables

def getUbicaciones():

    '''
    Se extrae la informacion de las ubicacioens en un objeto de trazables
    para ser guardada en el localStorage.

    Se almacena la informacion de forma bidireccional es decir se guarda la
    informacion de donde esta ubicado en el trazable y se crea una lista
    trazables contenido en la ubicacion
    '''

    url = Config.EndPoints.SINCRONIZACION_UBICACIONES
    request = getRequestTrazable(url)
    Data = request['data']
    Length = request['count'] 

    storage = localStorage()
    trazables = Information_Trazables()
    trazables = storage.get_Trazables()

    getData(Data, trazables)

    storage.set_Fincas(trazables.Information_Fincas)
    storage.set_Potreros(trazables.Information_Potreros)
    storage.set_Bovinos(trazables.Information_Bovinos) 

def getData(Data, trazables):
    
    for ubicacion in Data:
        
        key_ubication = ubicacion['ubicacion']
        element = ubicacion['elemento']
        type_of_Trazable = trazables.Type_of_Trazable(key_ubication)
        
        if type_of_Trazable == Config.Trazables.FINCA:
            trazableUbicacion = trazables.Information_Fincas
            insert_Element_Finca(trazables, trazableUbicacion, key_ubication, element)

def insert_Element_Finca(trazables, trazableUbicacion, key_ubication, element):
    
    type_of_element = trazables.Type_of_Trazable(element)
    list_of_element = "elements_"+type_of_element
    cant_of_element = "Cantidad_"+type_of_element

    if type_of_element == Config.Trazables.BOVINO:
        insert_Bov_Ubicacion(trazables, element, key_ubication)
        
    if list_of_element not in trazables.Information_Fincas[key_ubication]:
        trazableUbicacion[key_ubication][list_of_element] = []
    
    if cant_of_element not in trazables.Information_Fincas[key_ubication]:
        trazableUbicacion[key_ubication][cant_of_element] = 0

    trazableUbicacion[key_ubication][list_of_element].append(element)
    trazableUbicacion[key_ubication][cant_of_element] += 1

def insert_Bov_Ubicacion(trazables, element, key_ubication):
    trazables.Information_Bovinos[element]['ubication'] = key_ubication 