# Archivo que sirve como vista
import os
from dao.ProductoDAO import ProductoDAO
from models.Producto import Producto

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
    
def actualizar_producto():
    print('==== Actualizar producto ====')
    # solicitar nuevos datos
    codigo = input('Ingrese codigo a buscar: ')
    # intanciar producto
    p = Producto(codigo=codigo)
    # Validar si codigo existe
    dao = ProductoDAO(p)
    if dao.validar_codigo():
        nuevo_nombre = input('Ingrese nuevo nombre: ')
        nuevo_precio = input('Ingrese nuevo precio: ')
        nuevo_stock = input('Ingrese nuevo stock: ')
        p.nombre = nuevo_nombre
        p.precio = nuevo_precio
        p.stock = nuevo_stock
        dao.actualizar_producto()
    else:
        print('No se encontro producto')

def eliminar_producto():
    print('==== Eliminar producto ====')
    codigo = input('Ingrese codigo a buscar: ')
    # intanciar producto
    p = Producto(codigo=codigo)
    # Validar si codigo existe
    dao = ProductoDAO(p)
    if dao.validar_codigo():
        dao.eliminar_producto()
    else:
        print('No se encontro producto a eliminar')

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
            actualizar_producto()
            
        elif opcion == '4':
            eliminar_producto()
        
        elif opcion == '0':
            print('Saliendo de sistema...')
            break
            
        else:
            print('Debe ingresar una opcion valida...')
            
        input('Presione enter para continuar...')
    
menu_principal()