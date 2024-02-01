'''
En este archivo se muestran las constasntes que existes en la API
'''

class EndPoints:
    PATH = 'https://api.trazii.com'
    LOGIN = PATH + "/seguridad/auth/login"
    SINCRONIZACION_INVENTARIOS = PATH + "/sincronizacion/inventarios/"
    SINCRONIZACION_DATOS = PATH + "/sincronizacion/datos/"
    SINCRONIZACION_UBICACIONES = PATH + "/sincronizacion/ubicaciones/"
    SINCRONIZACION_TRAZAS = PATH + "/sincronizacion/trazas/"
    SINCRONIZACION_CARACTERISICAS = PATH + "/sincronizacion/caracteristicas/"

class GlobalVars:
    TYPE_OF_TOKEN = "Bearer"
    AGRONEGOCIO_BOVINO = "BV"
    
    Cantidades = {
    "Cant_BOV" : 0,
    "Cant_POT" : 0,
    "Cant_FIN" : 0,
    "Cant_COL" : 0,
    "Cant_GAN" : 0,
    "Cant_PRO" : 0,
    }

class Trazables:
    BOVINO = "BOV"
    GANADO = "GAN"
    POTRERO = "POT"
    FINCA = "FIN"
    COLABORADOR = "COL"
    PROPIETARIO = "PRO"

class Trazas: 
    ORDEÑO = 'ORDE'
    PESAJE = 'PEAN'
    SERVICIO = 'SERV'
    PALPACION = 'PALP'
    PARTO = 'PART'
    COMPRA = "COGA"
    VENDER = "VEGA"
    BAJA = "RESI"
    CELO = "RECE"
    SINTOMAS = "REST"
    PASTOREO = "POPA"

class EntidadesMetamodelo: 
    INVENTARIOS =  {
      "inquilino": "",
      "agronegocio": "",
      "trazable": "",
      "referencia": "",
      "denominacion": "",
      "padre": "",
      "estado": "",
      "ultimo_cambio": "",
      "id_trazii": ""
    }

    DATOS = {
        "valor": "",
        "estado": "",
        "ultimo_cambio": "",
        "inventario": "",
        "agronegocio": "",
        "trazable": "",
        "item": ""
    }

    UBICACIONES = {
        "ubicacion": "",
        "hasta": "",
        "observaciones": "",
        "referencia": "",
        "estado": "",
        "ultimo_cambio": "",
        "elemento": "",
        "desde": ""
    }

class Config(object):
    EndPoints = EndPoints
    Trazables = Trazables
    Trazas = Trazas
    GlobalVars = GlobalVars
    EntidadesMetamodelo = EntidadesMetamodelo