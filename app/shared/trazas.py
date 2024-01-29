from app.shared.constantsAPI import Config

class Information_Trazas:
    def __init__(self):
        self.Information_Ordeño = {}
        self.Information_Pesaje = {}
        self.Information_Servicio = {}
        self.Information_Palpacion = {}
        self.Information_Parto = {}
        self.Information_Compra = {}

    # Getter y Setter para Information_Ordeño
    def set_Ordeño(self, value):
        self.Information_Ordeño = value

    def get_Ordeño(self):
        return self.Information_Ordeño

    # Getter y Setter para Information_Servicio
    def set_Servicio(self, value):
        self.Information_Servicio = value

    def get_Servicio(self):
        return self.Information_Servicio

    # Getter y Setter para Information_Pesaje 
    def set_Pesaje(self, value):
        self.Information_Pesaje = value

    def get_Pesaje(self):
        return self.Information_Pesaje
    
    # Getter y Setter para Information_Compra 
    def set_Compra(self, value):
        self.Information_Compra = value
    
    def get_Compra(self):
        return self.Information_Compra
