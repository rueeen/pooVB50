class Persona:
    def __init__(self, rut:str = None, nombre:str = None, direccion:str = None):
        self.__rut = rut
        self.__nombre = nombre
        self.__direccion = direccion
        
    @property
    def rut(self):
        return self.__rut

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def direccion(self):
        return self.__direccion
    
    @rut.setter
    def rut(self, value):
        self.__rut = value
        
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @direccion.setter
    def direccion(self, value):
        self.__direccion = value