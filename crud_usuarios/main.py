import os

import mysql.connector
from models.Trabajador import Trabajador
from dao.TrabajadorDAO import TrabajadorDAO

def crear_trabajador():
    print('==== Registrando Trabajador ====')
    rut = input('Ingrese rut: ')
    nombre = input('Ingrese nombre: ')
    direccion = input('Ingrese direccion: ')
    usuario = input('Ingrese usuario: ')
    password = input('Ingrese password: ')
    sueldo_str = input('Ingrese sueldo: ')
    
    print('2. Administrador')
    print('3. Trabajador')
    rol_str = input('Ingrese rol: ')

    try:
        sueldo = int(sueldo_str)
    except ValueError:
        print("El sueldo debe ser un número entero.")
        return

    try:
        rol = int(rol_str)
    except ValueError:
        print("El rol debe ser un número entero (2 o 3).")
        return

    # --- Validaciones del modelo (ValueError del modelo) ---
    try:
        trabajador = Trabajador(
            rut=rut,
            nombre=nombre,
            direccion=direccion,
            usuario=usuario,
            password=password,
            sueldo=sueldo,
            id=rol
        )
    except ValueError as e:
        # Aquí llegan las validaciones de Persona/Trabajador (nombre vacío, usuario inválido, etc.)
        print(f"Error en datos del trabajador: {e}")
        return

    dao = None
    try:
        dao = TrabajadorDAO(trabajador)
        dao.crear_trabajador()
    except mysql.connector.Error as e:
        # Excepción específica de mysql.connector
        print(f"Error de base de datos al registrar trabajador: {e}")
    except Exception as e:
        # Cualquier otro error INESPERADO
        print(f"Error inesperado al registrar trabajador: {e}")
    finally:
        if dao is not None:
            dao.cerrar_dao()
def iniciar_sesion():
    print('==== Datos de usuario ====')
    usuario = input('Ingrese su usuario: ').lower()
    password = input('Ingrese su password: ')
    
    trabajador = None
    
    try:
        # Instanciando objeto tipo trabajador
        trabajador = Trabajador(usuario=usuario, password=password)
    except ValueError as e:
        print(e)
        return
        
    try:
        # Instanciamos objeto dao para trabajador
        dao = TrabajadorDAO(trabajador)
        if dao.iniciar_sesion():
            menu_principal(trabajador)
        else:
            print('Error en datos, intente nuevamente.')
    except:
        print('Error generico')
    finally:
        dao.cerrar_dao()

def menu_principal(trabajador: Trabajador):
    while True:
        # Limpiar pantalla
        os.system('cls')
        # Cargamos opciones
        print('==== Menu principal ====')
        print(f'Bienvenido: {trabajador.nombre}')
        print(type(trabajador.id))
        if trabajador.id == 2 or trabajador.id == 1:
            print('1. Crear usuarios')
        print('2. Ver datos')
        print('0. Cerrar sesion')
        
        opcion = input('Ingrese su opcion: ')
        os.system('cls')
        
        if opcion == '1' and (trabajador.id == 2 or trabajador.id == 1):
            crear_trabajador()
        
        elif opcion == '0':
            print(f'Hasta luego {trabajador.nombre}')
            trabajador = None
            break
        
        input('Presione enter para continuar...')
    
def menu_inicio_sesion():    
    while True:
        # Limpiar pantalla
        os.system('cls')
        # Cargamos opciones
        print('==== Inicio sesion ====')
        print('1. Iniciar sesion')
        print('0. Salir')
        
        opcion = input('Ingrese su opcion: ')
        os.system('cls')
        
        if opcion == '1':
            iniciar_sesion()
            
        input('Presione enter para continuar...')
    
    
menu_inicio_sesion()