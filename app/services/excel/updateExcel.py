from app.services.sync.trazables.request import getRequestTrazable
from app.shared.constantsAPI import Config

class UpdateExcel:
    def __init__(self):
        self.inventarios = []
        self.datos = []
        self.ubicaciones = []
    
    def updateInformation(self):

        for inv in self.inventarios:
            if inv['trazable'] == "POT":
                inv['denominacion'] = inv['denominacion'].split("_")[0] 
        
        urlInventarios = Config.EndPoints.SINCRONIZACION_INVENTARIOS
        urlDatos = Config.EndPoints.SINCRONIZACION_DATOS
        urlUbicaciones = Config.EndPoints.SINCRONIZACION_UBICACIONES

        #print("-----------------")
        #print("-----------------")
        #print("Inventario")
        #print(JsonInventario)

        #print()
        #print("-----------------")
        #print("-----------------")
        #print("Ubicaciones")
        #print(JsonUbicaciones)
        #print()

        #print("-----------------")
        #print("-----------------")
        #print("Datos")
        #print(JsonDatos)
        #print()

        print("\n ::: Inventariosa ::: \n")
        getRequestTrazable(urlInventarios, self.inventarios)

        print("\n ::: Ubicaciones ::: \n")
        getRequestTrazable(urlUbicaciones, self.ubicaciones)

        print("\n ::: Datos ::: \n")
        getRequestTrazable(urlDatos, self.datos)
