class Giro:
    def __init__(self, id=0, nroCuenta=0, cargo=0, saldo=0):
        self.__id = id
        self.__nroCuenta = nroCuenta
        self.__cargo = cargo
        self.__saldo = saldo
        
    @property
    def id(self):
        return self.__id
    
    @property
    def nroCuenta(self):
        return self.__nroCuenta
    
    @property
    def cargo(self):
        return self.__cargo
    
    @property
    def saldo(self):
        return self.__saldo