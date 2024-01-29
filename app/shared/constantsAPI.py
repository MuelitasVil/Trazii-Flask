'''
En este archivo se muestran las constasntes que existes en la API
'''

class EndPoints:
    PATH = 'https://api.trazii.com/'
    END_POINT_LOGIN = PATH + "/seguridad/auth/login"
    END_POINT_SINCRONIZACION_INVENTARIOS = PATH + "/sincronizacion/inventarios/"
    END_POINT_SINCRONIZACION_DATOS = PATH + "/sincronizacion/datos/"
    END_POINT_SINCRONIZACION_UBICACIONES = PATH + "/sincronizacion/ubicaciones/"
    END_POINT_SINCRONIZACION_TRAZAS = PATH + "/sincronizacion/trazas/"
    END_POINT_SINCRONIZACION_CARACTERISICAS = PATH + "/sincronizacion/caracteristicas/"

class GlobalVars:
    TYPE_OF_TOKEN = "Bearer"
    AGRONEGOCIO_BOVINO = "BV"
    Cantidades = {
    "cantidadBovinos" : 0,
    "cantidadPotreros" : 0,
    "cantidadFincas" : 0,
    "cantidadColaboradores" : 0,
    "cantidadGanado" : 0,
    "cantidadPropietarios" : 0,
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