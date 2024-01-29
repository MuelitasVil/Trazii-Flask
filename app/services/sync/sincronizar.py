from app.shared.localStorage import localStorage
from app.services.sync.datos import getDatos
from app.services.sync.ubicaciones import getUbicaciones
from app.services.sync.trazas import getTrazas
from app.services.sync.caracteristicas import getCaracteristicas

'''
Se cargan los datos en localStorage al llamar los datos en el orden estipulado 
en trazas se define la llave primaria del trazable en getDatos y la llave primaria
de trazas se define en getTrazas.
'''

def sincronizar_datos():
    
    # trazables
    getDatos()
    getUbicaciones()
    
    # trazas
    getTrazas()
    getCaracteristicas()
