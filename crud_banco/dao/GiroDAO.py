from models.Conexion import Conexion
from models.Giro import Giro


class GiroDAO:
    def __init__(self, giro:Giro):
        self.__conn = Conexion()
        self.__giro = giro
    
    def insertar_giro(self):
        sql = 'INSERT INTO giro(nroCuenta, cargo, saldo) VALUES (%s, %s, %s)'
        datos = (self.__giro.nroCuenta, self.__giro.cargo, self.__giro.saldo)
        if self.__conn.ejecutar(sql, datos):
            return True
        return False
    
    def mostrar_giros(self):
        sql = 'SELECT * FROM giro WHERE nroCuenta = %s'
        dato = (self.__giro.nroCuenta, )
        giros = self.__conn.listar(sql, dato)
        for giro in giros:
            print(f'ID transaccion: {giro["id"]}')
            print(f'Numero cuenta: {giro["nroCuenta"]}')
            print(f'Cargo: {giro["cargo"]}')
            print(f'Saldo: {giro["saldo"]}')
            print('-'*60)