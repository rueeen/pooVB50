# Archivo que sirve como vista
import os

from dao.ProductoDAO import ProductoDAO
from models.Producto import Producto

def menu_principal():
    while True:
        os.system('cls') # os.system('clear')
        print('==== Menu principal ====')
        print('1. Crear producto      C')
        print('2. Listar productos    R')
        print('3. Actualizar producto U')
        print('4. Eliminar producto   D')
        print('0. Salir')
        
        opcion = input('Ingrese su opcion: ')
        os.system('cls')
        
        if opcion == '1':
            agrega_producto()
            
        elif opcion == '2':
            listar_productos()
            
        elif opcion == '3':
            print('==== Actualizar productos ====')
            
        elif opcion == '4':
            print('==== Eliminar productos ====')
        
        elif opcion == '0':
            print('Saliendo de sistema...')
            break
            
        else:
            print('Debe ingresar una opcion valida...')
            
        input('Presione enter para continuar...')

def agrega_producto():
    print('==== Crear producto ====')
    codigo = input('Ingrese codigo de producto: ')
    nombre = input('Ingrese nombre de producto: ')
    precio = float(input('Ingrese precio de producto: '))
    stock = int(input('Ingrese stock de producto: '))
    # instancie un objeto de tipo producto
    producto = Producto(codigo=codigo, nombre=nombre, precio=precio, stock=stock)
    dao = ProductoDAO(producto)
    dao.insertar_producto()
    
def listar_productos():
    print('==== Listar productos ====')
    dao = ProductoDAO()
    dao.listar_productos()
    
menu_principal()