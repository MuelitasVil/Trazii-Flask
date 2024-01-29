from app.shared.constantsAPI import Config

class Information_Trazables:
    def __init__(self):
        self.Information_Bovinos = {}
        self.Information_Potreros = {}
        self.Information_Fincas = {}
        self.Information_Colaboradores = {}
        self.Information_Ganado = {}
        self.Information_Propietarios = {}
    
    # Getter y Setter para Information_Bovinos
    def get_Bovinos(self):
        return self.Information_Bovinos

    def set_Bovinos(self, value):
        self.Information_Bovinos = value

    # Getter y Setter para Information_Potreros
    def get_Potreros(self):
        return self.Information_Potreros

    def set_Potreros(self, value):
        self.Information_Potreros = value

    # Getter y Setter para Information_Fincas
    def get_Fincas(self):
        return self.Information_Fincas

    def set_Fincas(self, value):
        self.Information_Fincas = value

    # Getter y Setter para Information_Colaboradores
    def get_Colaboradores(self):
        return self.Information_Colaboradores

    def set_Colaboradores(self, value):
        self.Information_Colaboradores = value

    # Getter y Setter para Information_Ganado
    def get_Ganado(self):
        return self.Information_Ganado

    def set_Ganado(self, value):
        self.Information_Ganado = value

    # Getter y Setter para Information_Propietarios
    def get_Propietarios(self):
        return self.Information_Propietarios

    def set_Propietarios(self, value):
        self.Information_Propietarios = value

    # Verificar tipo de trazable :  
    def Type_of_Trazable(self , key):

        if self.IsPotrero(key):
            return Config.Trazables.POTRERO 

        if self.IsFinca(key):
            return Config.Trazables.FINCA
        
        if self.IsGanado(key):
            return Config.Trazables.GANADO

        if self.IsBovino(key):
            return Config.Trazables.BOVINO
        
        if self.IsColaborador(key):
            return Config.Trazables.COLABORADOR

        if self.IsPropietario(key):
            return Config.Trazables.PROPIETARIO
        
        return "NONE"   
    
    def IsBovino(self, key):
        if key in self.Information_Bovinos:
            return True
        return False

    def IsGanado(self, key):
        if key in self.Information_Ganado:
            return True
        return False
    
    def IsColaborador(self, key):
        if key in self.Information_Colaboradores:
            return True
        return False

    def IsPropietario(self, key):
        if key in self.Information_Propietarios:
            return True
        return False

    def IsPotrero(self, key):
        if key in self.Information_Potreros:
            return True
        return False
    
    def IsFinca(self, key):
        if key in self.Information_Fincas:
            return True
        return False
