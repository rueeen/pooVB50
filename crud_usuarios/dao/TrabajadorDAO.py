import mysql.connector
from models.Conexion import Conexion
from models.Trabajador import Trabajador

class TrabajadorDAO:
    def __init__(self, trabajador: Trabajador):
        self.__conexion = Conexion()
        self.__trabajador = trabajador
        
    def iniciar_sesion(self):
        sql = '''
        SELECT p.rut, p.nombre, t.sueldo, p.direccion, t.id
        FROM persona p JOIN trabajador t 
        ON p.rut = t.rut
        WHERE usuario = %s AND password = %s
        '''
        try:
            datos = self.__conexion.listar_uno(
                sql, 
                (self.__trabajador.usuario, self.__trabajador.password)
            )
            if datos:
                self.__trabajador.rut = datos['rut']
                self.__trabajador.sueldo = datos['sueldo']
                self.__trabajador.nombre = datos['nombre']
                self.__trabajador.direccion = datos['direccion']
                self.__trabajador.id = datos['id']
                return True
            return False
        except mysql.connector.Error as e:
            print(f"Error al iniciar sesión en la base de datos: {e}")
            return False

    def crear_trabajador(self):
        sql_persona = 'INSERT INTO persona(rut, nombre, direccion) VALUES (%s, %s, %s)'
        sql_trabajador = '''
            INSERT INTO trabajador(rut, usuario, id, password, sueldo) 
            VALUES (%s, %s, %s, %s, %s)
        '''
        try:
            datos_persona = (
                self.__trabajador.rut,
                self.__trabajador.nombre,
                self.__trabajador.direccion
            )
            if self.__conexion.ejecutar(sql_persona, datos_persona):
                datos_trabajador = (
                    self.__trabajador.rut,
                    self.__trabajador.usuario,
                    self.__trabajador.id,
                    self.__trabajador.password,
                    self.__trabajador.sueldo
                )
                if self.__conexion.ejecutar(sql_trabajador, datos_trabajador):
                    print('Se creó trabajador')
                else:
                    print('No se logró crear trabajador (tabla trabajador)')
            else:
                print('No se logró crear persona (tabla persona)')
        except mysql.connector.Error as e:
            print(f'Error de base de datos al crear trabajador: {e}')
