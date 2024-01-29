from localStoragePy import localStoragePy
from flask import session
import requests
import json
import jwt

from app.shared.constantsAPI import Config
from app.shared.localStorage import localStorage


def Login(data):
    response = requests.post(Config.EndPoints.END_POINT_LOGIN, data = json.dumps(data)).json()
    
    if("detail" in response):
        return False
    
    token = response["access_token"]
    decoded_data = jwt.decode(jwt=token, algorithms=["HS256"], options={"verify_signature": False})
    subject_data = decoded_data["subject"]
    expirationTime = decoded_data["exp"]
    
    session['usuario'] = subject_data['telefono']

    storage = localStorage()
    
    storage.set_subject_data(subject_data)
    storage.set_token(token)
    storage.set_exp(expirationTime)

    print("Informacion del usuario : ")
    print(subject_data)
    print(token)

    return True
