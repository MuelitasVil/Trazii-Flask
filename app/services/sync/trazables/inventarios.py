from app.services.sync.trazables.request import getRequestTrazable
from app.shared.localStorage import localStorage
from app.shared.constantsAPI import Config

def getEndPointInventarios(Informacion = []):

    '''
    Se extrae la informacion de los datos en un objeto de trazables
    para ser guardada en el localStorage.

    Ademas se cuenta la cantidad de articulos que tiene un trazable
    '''

    url = Config.EndPoints.SINCRONIZACION_INVENTARIOS
    getRequestTrazable(url)