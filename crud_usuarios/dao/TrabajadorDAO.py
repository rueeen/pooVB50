import mysql.connector
from models.Conexion import Conexion
from models.Trabajador import Trabajador

class TrabajadorDAO:
    def __init__(self, trabajador:Trabajador):
        self.__conexion = Conexion()
        self.__trabajador = trabajador
        
    def iniciar_sesion(self):
        sql = '''
        SELECT p.rut, p.nombre, t.sueldo, p.direccion, t.id
        FROM persona p JOIN trabajador t 
        ON p.rut = t.rut
        WHERE usuario = %s AND password = %s'''
        try:
            datos = self.__conexion.listar_uno(sql, (self.__trabajador.usuario, self.__trabajador.password))
            if datos:
                self.__trabajador.rut = datos['rut']
                self.__trabajador.sueldo = datos['sueldo']
                self.__trabajador.nombre = datos['nombre']
                self.__trabajador.direccion = datos['direccion']
                self.__trabajador.id = datos['id']
                return True
            return False
        except:
            print('Error en la consulta')
    
    def cerrar_dao(self):
        self.__conexion.cerrar_conexion()
        
    def crear_trabajador(self):
        sql = 'INSERT INTO persona(rut, nombre, direccion) VALUES (%s, %s, %s)'
        try:
            datos = (self.__trabajador.rut, self.__trabajador.nombre, self.__trabajador.direccion)
            if self.__conexion.ejecutar(sql, datos):
                sql = 'INSERT INTO trabajador(rut, usuario, id, password, sueldo) VALUES (%s, %s, %s, %s, %s)'
                datos = (self.__trabajador.rut, self.__trabajador.usuario, self.__trabajador.id, self.__trabajador.password, self.__trabajador.sueldo)
                if self.__conexion.ejecutar(sql, datos):
                    print('Se creo trabajador')
                else:
                    print('No se logro crear trabajador')
        except mysql.connector.errors as e:
            print(f'{e}')
            