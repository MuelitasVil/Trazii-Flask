import httpx
import json

from app.shared.localStorage import localStorage
from app.shared.constantsAPI import Config

def getRequestTrazable(url, Informacion = []):

    '''
    Usando localStorage se llama la informacion del token y del inquilino.
    '''

    storage = localStorage()
    token = storage.get_token()
    subject_data = storage.get_subject_data()

    params = {
        "inquilino" : subject_data["inquilino"],
    }

    headers = {
        'Authorization': "{} {}".format(Config.GlobalVars.TYPE_OF_TOKEN, token),
        'agronegocio' : Config.GlobalVars.AGRONEGOCIO_BOVINO
    }

    data = json.dumps(Informacion, ensure_ascii=False)
    
    with httpx.Client() as client:
        response = client.post(
            url,
            headers = headers,
            params = params,
            data = data
            ).json()
    
    print("Repuesta : ")
    print(response)
    
    return response
