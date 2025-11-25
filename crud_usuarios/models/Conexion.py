# pip install mysql-connector-python
import mysql.connector

class Conexion:
    def __init__(self):
        # Creando conexion a base de datos
        self.__conn = mysql.connector.connect(
            # Cadena de conexion
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'gestion_personas'
        )
    
    '''
    def probar_conexion(self):
        cursor = self.__conn.cursor()
        cursor.execute("SHOW TABLES")
        for table in cursor:
            print(table)
    '''    
        
    # Sirve para INSERT, UPDATE, DELETE
    def ejecutar(self, sql:str, datos=None):
        try:
            cursor = self.__conn.cursor() # Crea objeto tipo cursor
            cursor.execute(sql, datos)
            self.__conn.commit() # confirma cambios
            if cursor.rowcount > 0:
                return True
            return False
        except mysql.connector.errors as e:
            print(f'Se produjo un error: {e}')
            return False
        finally:
            cursor.close()
    
    def listar(self, sql:str, datos=None):
        '''
        Este metodo devuele una lista de diccionarios
        [{codigo:1111, nombre:'lavadora', precio:35000, stock:3}, {codigo:1112, nombre:'Television', precio:45000, stock:3}]
        '''
        try:
            cursor = self.__conn.cursor(dictionary=True)
            if datos:
                cursor.execute(sql, datos)
            else:
                cursor.execute(sql)
            return cursor.fetchall()
        except mysql.connector.errors as e:
            print(f'Se produjo un error: {e}')
            return []
        finally:
            cursor.close()
    
    def listar_uno(self, sql:str, datos=None):
        '''
        Este metodo devuele un diccionario
        {codigo:1111, nombre:'lavadora', precio:35000, stock:3}
        '''
        try:
            cursor = self.__conn.cursor(dictionary=True)
            cursor.execute(sql, datos)
            return cursor.fetchone()
        except mysql.connector.errors as e:
            print(f'Se produjo un error: {e}')
            return {}
        finally:
            cursor.close()

    def cerrar_conexion(self):
        if self.__conn is not None:
            self.__conn.close()