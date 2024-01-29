import requests
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

    storage = localStorage()
    
    subject_data = storage.get_subject_data()
    token = storage.get_token()

    params = {
        "inquilino" : subject_data["inquilino"],
    }

    headers = {
        'Authorization': "{} {}".format(Config.GlobalVars.TYPE_OF_TOKEN, token),
        'agronegocio' : Config.GlobalVars.AGRONEGOCIO_BOVINO
    }

    request = requests.post(
        Config.EndPoints.END_POINT_SINCRONIZACION_UBICACIONES,
        params = params,
        json = [],
        headers = headers).json()
    
    Data = request['data']
    Length = request['count']

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
            insert_Element_Finca(trazables, key_ubication, element)
        
        if type_of_Trazable == Config.Trazables.POTRERO:
            insert_Element_Potreros(trazables, key_ubication, element)

def insert_Element_Finca(trazables, key_ubication, element):
    
    type_of_element = trazables.Type_of_Trazable(element)
    list_of_element = "elements_"+type_of_element
    cant_of_element = "Cantidad_"+type_of_element

    if type_of_element == Config.Trazables.BOVINO:
        insert_Bov_Ubicacion(trazables, element, key_ubication)
        
    if list_of_element not in trazables.Information_Fincas[key_ubication]:
        trazables.Information_Fincas[key_ubication][list_of_element] = []
    
    if cant_of_element not in trazables.Information_Fincas[key_ubication]:
        trazables.Information_Fincas[key_ubication][cant_of_element] = 0

    trazables.Information_Fincas[key_ubication][list_of_element].append(element)
    trazables.Information_Fincas[key_ubication][cant_of_element] += 1

def insert_Element_Potreros(trazables, key_ubication, element):

    type_of_element = trazables.Type_of_Trazable(element)
    list_of_element = "elements_"+type_of_element
    cant_of_element = "Cantidad_"+type_of_element

    if list_of_element not in trazables.Information_Potreros[key_ubication]:
        trazables.Information_Potreros[key_ubication][list_of_element] = []

    if cant_of_element not in trazables.Information_Potreros[key_ubication]:
        trazables.Information_Potreros[key_ubication][cant_of_element] = 0
        
    trazables.Information_Potreros[key_ubication][list_of_element].append(element)
    trazables.Information_Fincas[key_ubication][cant_of_element] += 1

def insert_Bov_Ubicacion(trazables, element, key_ubication):
    trazables.Information_Bovinos[element]['ubication'] = key_ubication 