from models.Conexion import Conexion
from models.Trabajador import Trabajador

class TrabajadorDAO:
    def __init__(self, trabajador:Trabajador):
        self.__conexion = Conexion()
        self.__trabajador = trabajador
        
    def iniciar_sesion(self):
        sql = '''
        SELECT p.rut, p.nombre, t.sueldo, p.direccion 
        FROM persona p JOIN trabajador t 
        ON p.rut = t.rut; 
        WHERE usuario = %s AND password = %s'''
        datos = self.__conexion.listar_uno(sql, (self.__trabajador.usuario, self.__trabajador.password))
        if datos:
            self.__trabajador.rut = datos['rut']
            self.__trabajador.sueldo = datos['sueldo']
            self.__trabajador.nombre = datos['nombre']
            self.__trabajador.direccion = datos['direccion']
            return True
        return False