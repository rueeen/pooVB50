import os

from models.Trabajador import Trabajador

from dao.TrabajadorDAO import TrabajadorDAO

def iniciar_sesion():
    print('==== Datos de usuario ====')
    usuario = input('Ingrese su usuario: ').lower()
    password = input('Ingrese su password: ')
    # Instanciando objeto tipo trabajador
    trabajador = Trabajador(usuario=usuario, password=password)
    # Instanciamos objeto dao para trabajador
    dao = TrabajadorDAO(trabajador)
    if dao.iniciar_sesion():
        menu_principal(trabajador)
    else:
        print('Error en datos, intente nuevamente.')

def menu_principal(trabajador: Trabajador):
    while True:
        # Limpiar pantalla
        os.system('cls')
        # Cargamos opciones
        print('==== Menu principal ====')
        print(f'Bienvenido: {trabajador.nombre}')
        print('1. ')
        print('2. ')
        print('0. Cerrar sesion')
        
        opcion = input('Ingrese su opcion: ')
        os.system('cls')
        
        if opcion == '0':
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