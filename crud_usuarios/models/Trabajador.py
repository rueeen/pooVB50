from models.Persona import Persona

class Trabajador(Persona):
    def __init__(self, rut = None, nombre = None, direccion = None, usuario:str = None, password:str = None, sueldo:int = None):
        super().__init__(rut, nombre, direccion)
        self.__usuario = usuario
        self.__password = password
        self.__sueldo = sueldo
        
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def password(self):
        return self.__password
    
    @property
    def sueldo(self):
        return self.__sueldo
    
    @usuario.setter
    def usuario(self, value):
        self.__usuario = value
    
    @password.setter
    def password(self, value):
        self.__password = value
        
    @sueldo.setter
    def sueldo(self, value):
        self.__sueldo = value