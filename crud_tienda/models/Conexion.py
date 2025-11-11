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
            database = 'tienda'
        )
        
    def probar_conexion(self):
        cursor = self.__conn.cursor()
        cursor.execute("SHOW TABLES")
        for table in cursor:
            print(table)
        
    # Sirve para INSERT, UPDATE, DELETE
    def ejecutar(self, sql:str, datos=None):
        cursor = self.__conn.cursor() # Crea objeto tipo cursor
        cursor.execute(sql, datos)
        self.__conn.commit() # confirma cambios
        if cursor.rowcount > 0:
            return True
        return False
    
    def listar(self, sql:str):
        cursor = self.__conn.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchall()