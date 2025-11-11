from models.Conexion import Conexion
from models.Producto import Producto

class ProductoDAO:
    def __init__(self, producto:Producto = None):
        self.__conexion = Conexion()
        self.__producto = producto # instancia de clase producto recibida desde main.py
        
    def insertar_producto(self):
        sql = 'INSERT INTO producto(codigo, nombre, precio, stock) VALUES (%s, %s, %s, %s)'
        datos = (self.__producto.codigo, self.__producto.nombre, self.__producto.precio, self.__producto.stock)
        if self.__conexion.ejecutar(sql, datos):
            print('Producto registrado')
        else:
            print('Produto no se logro registrar')
            
    def listar_productos(self):
        sql = 'SELECT codigo, nombre, precio, stock FROM producto'
        lista = self.__conexion.listar(sql)
        for producto in lista: # [ {'codigo':'111', 'nombre':'lavadora',....}]
            print(f'Codigo: {producto["codigo"]}')
            print(f'Nombre: {producto["nombre"]}')
            print(f'Precio: {producto["precio"]}')
            print(f'Stock: {producto["stock"]}')
            print('*'*50)