from models.Conexion import Conexion
from models.Cuenta import Cuenta

class CuentaDAO:
    def __init__(self, cuenta:Cuenta):
        self.__conn = Conexion()
        self.__cuenta = cuenta
        
    def mostrar_cuentas(self):
        sql = 'SELECT * FROM cuenta'
        lista = self.__conn.listar(sql)
        for cuenta in lista:
            print(f'Numero cuenta: {cuenta["nroCuenta"]}')
            print(f'Monto: {cuenta["monto"]}')
            print('-'*60)
            
    def traer_monto(self):
        sql = 'SELECT monto FROM cuenta WHERE nroCuenta = %s'
        datos = (self.__cuenta.nroCuenta,)
        print(datos)
        return self.__conn.listar_uno(sql, datos)['monto'] # {'monto':300000}
        
    def actualizar_saldo(self):
        sql = 'UPDATE cuenta SET monto = %s WHERE nroCuenta = %s'
        datos = (self.__cuenta.monto, self.__cuenta.nroCuenta)
        if self.__conn.ejecutar(sql, datos):
            print('Se actualizo saldo cuenta')
        else:
            print('No se logro actualizar saldo. Favor contacte a soporte')
            
    def mostrar_cuenta(self):
        sql = 'SELECT * FROM cuenta WHERE nroCuenta = %s'
        dato = (self.__cuenta.nroCuenta, )
        cuenta = self.__conn.listar_uno(sql, dato)
        print(f'Numero cuenta: {cuenta["nroCuenta"]}')
        print(f'Monto: {cuenta["monto"]}')
        print('-'*60)