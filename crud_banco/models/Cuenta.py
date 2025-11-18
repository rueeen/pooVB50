class Cuenta:
    def __init__(self, nroCuenta:int=0, monto:int=0):
        self.__nroCuenta = nroCuenta
        self.__monto = monto
        
    @property
    def nroCuenta(self):
        return self.__nroCuenta
        
    @property
    def monto(self):
        return self.__monto  
        
    @nroCuenta.setter
    def nroCuenta(self, value):
        self.__nroCuenta = value
    
    @monto.setter
    def monto(self, value):
        self.__monto = value
        
    def __str__(self):
        return (f'Datos objeto: {self.__nroCuenta} - {self.__monto}')