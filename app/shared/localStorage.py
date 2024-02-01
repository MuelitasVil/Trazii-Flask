from localStoragePy import localStoragePy
from flask import session
import ast

from app.shared.trazables import Information_Trazables
from app.shared.trazas import Information_Trazas


class localStorage:
    
    def __init__(self):
        usuario = session['usuario']
        self.Storage = localStoragePy('UserData' + str(usuario), 'json') 
        
    # Limpiar el localStorage 
    def Clean(self):
        self.Storage.clear()
        
    # -------------------- Usuario --------------------
        
    # Datos del usuario:
    def set_subject_data(self, subject_data): 
        self.Storage.setItem("subject_data", subject_data)

    def get_subject_data(self):
        return ast.literal_eval(self.Storage.getItem("subject_data"))
    
    # Datos del token : 
    def set_token(self, token):
        self.Storage.setItem("token", token)

    def get_token(self):
        return self.Storage.getItem("token")
    
    def set_exp(self, exp):
        self.Storage.setItem("exp", exp)
    
    def get_exp(self):
        return self.Storage.getItem("exp")
    
    # -------------------- Trazables --------------------

    # Datos de los bovinos : 
    def set_Bovinos(self, Information_Bovinos):
        self.Storage.setItem("Information_Bovinos",Information_Bovinos)
    
    def get_Bovinos(self):
        return ast.literal_eval(self.Storage.getItem("Information_Bovinos"))
    
    # Datos de los potreros : 
    def set_Potreros(self, Information_Potreros):
        self.Storage.setItem("Information_Potreros", Information_Potreros)
    
    def get_Potreros(self):
        return ast.literal_eval(self.Storage.getItem("Information_Potreros"))
    
    # Datos de las fincas : 
    def set_Fincas(self, Information_Fincas):
        self.Storage.setItem("Information_Fincas", Information_Fincas)
    
    def get_Fincas(self):
        return ast.literal_eval(self.Storage.getItem("Information_Fincas"))
    
    # Datos de los colaboradores :
    def set_Colaboradores(self, Information_Colaboradores):
        self.Storage.setItem("Information_Colaboradores", Information_Colaboradores)
   
    def get_Colaboradores(self):
        return ast.literal_eval(self.Storage.getItem("Information_Colaboradores"))
     
    # Datos del ganado : 
    def set_Ganado(self, Information_Ganado):  
        self.Storage.setItem("Information_Ganado", Information_Ganado)
    
    def get_Ganado(self):
        return ast.literal_eval(self.Storage.getItem("Information_Ganado"))
    
    # Datos de los propietarios :  
    def set_Propietarios(self, Information_Propietarios):
        self.Storage.setItem("Information_Propietarios",Information_Propietarios)

    def get_Propietarios(self):
        return ast.literal_eval(self.Storage.getItem("Information_Propietarios"))
    
    # clase Trazables : 
    def get_Trazables(self):
        trazables = Information_Trazables()
        trazables.set_Bovinos(self.get_Bovinos()) 
        trazables.set_Potreros(self.get_Potreros())  
        trazables.set_Fincas(self.get_Fincas())
        trazables.set_Colaboradores(self.get_Colaboradores())
        trazables.set_Ganado(self.get_Ganado())
        trazables.set_Propietarios(self.get_Propietarios())
        return trazables
    
    def set_trazables(self, Trazables):
        self.set_Bovinos(Trazables.Information_Bovinos) 
        self.set_Colaboradores(Trazables.Information_Colaboradores)
        self.set_Fincas(Trazables.Information_Fincas)
        self.set_Ganado(Trazables.Information_Ganado)
        self.set_Potreros(Trazables.Information_Potreros)
        self.set_Propietarios(Trazables.Information_Propietarios)

    # Cantidades de trazables 
    def set_Cantidades(self, Cantidades):
        self.Storage.setItem("Cantidades", Cantidades)

    def get_Cantidades(self):
        return ast.literal_eval(self.Storage.getItem("Cantidades"))
    
    # -------------------- Trazas --------------------

    # datos de ordeño 
    def set_Ordeño(self, Information_Ordeño):
        self.Storage.setItem("Information_Ordeño", Information_Ordeño)
    
    def get_Ordeño(self):
        return ast.literal_eval(self.Storage.getItem("Information_Ordeño"))

    # datos de pesaje 
    def set_Pesaje(self, Information_Pesaje):
        self.Storage.setItem("Information_Pesaje", Information_Pesaje)

    def get_Pesaje(self):
        return ast.literal_eval(self.Storage.getItem("Information_Pesaje"))

    # datos del servicio
    def set_Servicio(self, Information_Servicio):
        self.Storage.setItem("Information_Servicio", Information_Servicio)

    def get_Servicio(self):
        return ast.literal_eval(self.Storage.getItem("Information_Servicio"))
    
    # datos de la palpacion : 
    def set_Palpacion(self, Information_Palpacion):
        self.Storage.setItem("Information_Palpacion", Information_Palpacion)

    def get_Palpacion(self, Information_Palpacion):
        return ast.literal_eval(self.Storage.getItem("Information_Palpacion"))
    
    # datos del parto
    def set_Parto(self, Information_Parto):
        self.Storage.setItem("Information_Parto", Information_Parto)

    def get_Parto(self):
        return ast.literal_eval(self.Storage.getItem("Information_Parto"))

    # datos de la compra 
    def set_Compra(self, Information_Compra):
        self.Storage.setItem("Information_Compra", Information_Compra)
    
    def get_Compra(self):
        return ast.literal_eval(self.Storage.getItem("Information_Compra"))
    
    # Clase de trazas 
    def get_Trazas(self):
        trazas = Information_Trazas()
        trazas.set_Ordeño(self.get_Ordeño())
        trazas.set_Pesaje(self.get_Pesaje())
        trazas.set_Servicio(self.get_Servicio())
        trazas.set_Compra(self.get_Compra())
        return trazas