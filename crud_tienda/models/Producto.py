class Producto:
    def __init__(self, codigo:str = '', nombre:str = '', precio:float = 0, stock:int = 0):
        # __ atributo privado
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
    
    @precio.setter
    def precio(self, value):
        self.__precio = value
        
    @stock.setter
    def stock(self, value):
        self.__stock = value