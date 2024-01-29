from app.shared.localStorage import localStorage
from app.shared.constantsAPI import Config
from app.services.excel.columnsToDB import columnsTODB
from datetime import datetime
import uuid

class ExceltoJson:
        
    def JsonInventario(self, filaExcel, nombreHoja, trazablesSubidos):

        '''
        Se va a recorrer la fila enviada por el excelManager y se va a 
        trasformar en un diccionario, con el fin de crear un Json.

        Ojo : El padre no necesariamente va ser nulo siempre en esta funcion
        sin embargo en esta funcion no es posible saber si tiene padre o no.
        '''

        Inventario = Config.EntidadesMetamodelo.INVENTARIOS.copy()
        storage = localStorage()        

        subject_data = storage.get_subject_data()
        
        inquilino = subject_data['inquilino']
        agronegocio = Config.GlobalVars.AGRONEGOCIO_BOVINO
        trazable = self.get_Trazable(nombreHoja)
        referencia = None
        denominacion = self.get_Denominacion(filaExcel, trazable)
        padre = None
        estado = "Activo"
        ultimo_cambio = self.get_ultimoCambio()
        id_trazii = self.get_uuid()

        Inventario['inquilino'] = inquilino 
        Inventario['agronegocio'] = agronegocio
        Inventario['trazable'] = trazable 
        Inventario['referencia'] = referencia
        Inventario['denominacion'] = denominacion
        Inventario['padre'] = padre
        Inventario['estado'] = estado
        Inventario['ultimo_cambio'] = ultimo_cambio
        Inventario['id_trazii'] = id_trazii 

        return Inventario

    def JsonDatos(self, filaExcel, headers, nombreHoja, uuid):
        trazable = self.get_Trazable(nombreHoja)
        estado = "Activo"
        ultimo_cambio = self.get_ultimoCambio()
        inventario = uuid
        agronegocio = "BV"

        DictColumnToItem = self.get_DictColumnToItem(trazable)
        Datos = []
        cantidad_datos = len(filaExcel)
        
        for i in range(cantidad_datos):
            dato = {}

            # Ignorar celda vacia 
            if filaExcel[i] == None:
                continue 

            # Ignorar celdas con padres o ubicaciones
            if headers[i] in ["*Finca", "*Lote"]:
                continue

            valor = filaExcel[i]
            item = DictColumnToItem[headers[i]]
            
            if isinstance(valor, datetime):
                valor = valor.strftime('%Y-%m-%dT%H:%M:%S')

            dato['valor'] = valor 
            dato['estado'] = estado
            dato['ultimo_cambio'] = ultimo_cambio
            dato['inventario'] = inventario
            dato['agronegocio'] = agronegocio
            dato['trazable'] = trazable
            dato['item'] = item
            
            Datos.append(dato)

        return Datos

    def JsonUbicacion(self, trazables):
        
        '''
        En el manejador de excel en un diccionario que se llama trazables se
        almacenan : 

        'id_trazii' : Id unico otorgado a elemento, en la base de datos
        'ubicacion' : Lugar donde se ubica el elemento
        'padre' : Padre del elemento 
        'elementos' : elementos ubicados en el elemento
        'hijos' : hijos del elemento
        
        Se van a recorrer los trazables que sean ubicaciones para construir el
        Json. 
        
        Actualmente la unica ubicacion es finca por lo tanto es el unico tipo 
        de trazable que se va a recorrer.
        '''

        trazablesUbicacion = trazables['FIN']
        ubicaciones = []
        
        for keyubicacicon in trazablesUbicacion:
            trazableUbicacion = trazablesUbicacion[keyubicacicon]
            elementosUbicacion = trazableUbicacion['elementos']
            ubicacion = trazableUbicacion['id_trazii']
            hasta = None 
            observaciones = None
            referencia = None
            estado = "Activo"
            ultimo_cambio = self.get_ultimoCambio()
            desde = self.get_ultimoCambio()

            for elemento in elementosUbicacion:
                ubicacionJson = {}
                ubicacionJson['ubicacion'] = ubicacion
                ubicacionJson['hasta'] = hasta
                ubicacionJson['observaciones'] = observaciones
                ubicacionJson['referencia'] = referencia
                ubicacionJson['estado'] = estado
                ubicacionJson['ultimo_cambio'] = ultimo_cambio
                ubicacionJson['elemento'] = elemento
                ubicacionJson['desde'] = desde
                ubicaciones.append(ubicacionJson)

        return ubicaciones

    def get_Denominacion(self,filaExcel, trazable):
        
        '''
        La denominacion de los trazables es ubicada puesto que se conoce el 
        excel, es decir si obseva el excel, el nombre de la finca esta en la 
        posicion C, es decir la posicion 0 del arreglo.
        '''

        if trazable == Config.Trazables.FINCA:
            return filaExcel[0] 
        if trazable == Config.Trazables.POTRERO:
            return str(filaExcel[0]) + "_" + str(filaExcel[1])
        if trazable == Config.Trazables.GANADO:
            return filaExcel[0]
        if trazable == Config.Trazables.BOVINO:
            return str(filaExcel[0]) + "_" + str(filaExcel[2])


    def get_DictColumnToItem(self, trazable):
        if trazable == Config.Trazables.FINCA:
            return columnsTODB.fincas.Items
        if trazable == Config.Trazables.POTRERO:
            return columnsTODB.potreros.Items
        if trazable == Config.Trazables.GANADO:
            return columnsTODB.lotes.Items
        if trazable == Config.Trazables.BOVINO:
            return columnsTODB.bovinos.Items
        
    def get_Trazable(self, nombreHoja):
        if nombreHoja == "FINCAS":
            return Config.Trazables.FINCA
        if nombreHoja == "POTREROS":
            return Config.Trazables.POTRERO
        if nombreHoja == "LOTES":
            return Config.Trazables.GANADO
        if nombreHoja == "GANADO":
            return Config.Trazables.BOVINO
        
    def get_ultimoCambio(self):
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    
    def get_uuid(self):
        return str(uuid.uuid4())
    