import requests
import ast
from app.shared.constantsAPI import Config
from localStoragePy import localStoragePy

def getInventarios():

    '''
    Se extrae la informacion de la sincronizacion de trazables sin embargo
    no se esta usando actualmente
    '''

    localStorage = localStoragePy('UserData', 'json')
    
    inventario = localStorage.getItem("Inventario")
    token = localStorage.getItem("token")
    
    data = ast.literal_eval(data)
    params = {
        "inquilino" : data["inquilino"],
    }

    headers = {
        'Authorization': "{} {}".format(Config.GlobalVars.TYPE_OF_TOKEN, token),
        'agronegocio' : Config.GlobalVars.AGRONEGOCIO_BOVINO
    }

    data = []
    request = requests.post(
        Config.EndPoints.END_POINT_SINCRONIZACION_INVENTARIOS,
        params = params,
        json = [],
        headers = headers).json()
    
    localStorage.setItem("Inventario", request['data'])
    localStorage.setItem("tam_inventario", request['count'])
    