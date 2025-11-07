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
            
c = Conexion()
c.probar_conexion()