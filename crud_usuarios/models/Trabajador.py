from models.Persona import Persona

class Trabajador(Persona):
    def __init__(self, rut = None, nombre = None, direccion = None, usuario:str = None, password:str = None, sueldo:int = None, id:int = None):
        super().__init__(rut, nombre, direccion)
        self.__usuario = self.validar_usuario(usuario)
        self.__password = password
        self.__sueldo = sueldo
        self.__id = id
        
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def password(self):
        return self.__password
    
    @property
    def sueldo(self):
        return self.__sueldo
    
    @property
    def id(self):
        return self.__id
    
    @usuario.setter
    def usuario(self, value):
        self.__usuario = value
    
    @password.setter
    def password(self, value):
        self.__password = value
        
    @sueldo.setter
    def sueldo(self, value):
        self.__sueldo = value
    
    @id.setter
    def id(self, value):
        self.__id = value
        
    def validar_usuario(self, usuario: str):
        if usuario is None:
            return
        
        if usuario.strip() == "":
            raise ValueError('Nombre de usuario no debe ser vacio')
        elif len(usuario) > 20:
            raise ValueError('Nombre de usuario no puede ser mayor a 10 caracteres')
        
        return usuario