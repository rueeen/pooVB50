import os

from dao.CuentaDAO import CuentaDAO
from dao.GiroDAO import GiroDAO
from models.Cuenta import Cuenta
from models.Giro import Giro

def realizar_giro():
    print('==== Realizar giro ====')
    # Mostrar todas las cuentas
    c = Cuenta()
    cuentaDAO = CuentaDAO(c)
    cuentaDAO.mostrar_cuentas()
    # Solicitar nroCuenta y monto
    nroCuenta = int(input('Ingrese numero de cuenta a girar: '))
    c.nroCuenta = nroCuenta
    cargo = int(input('Ingrese monto a girar: '))
    monto = cuentaDAO.traer_monto()
    # Validacion saldo
    if monto < cargo:
        print('Monto en cuenta insuficiente')
        return
    saldo = monto - cargo
    # Crear Giro
    giro = Giro(nroCuenta=nroCuenta, saldo=saldo, cargo=cargo)
    giroDAO = GiroDAO(giro)
    if giroDAO.insertar_giro():
        print('Se realizo giro')
        c.monto = saldo
        cuentaDAO.actualizar_saldo()
    else:
        print('No se logro registrar giro, intente nuevamente.')
        
def ver_saldos_cuenta():
    print('==== Ver saldos cuenta ====')
    nroCuenta = int(input('Ingrese numero cuenta a revisar: '))
    cuenta = Cuenta(nroCuenta=nroCuenta)
    cuentaDAO = CuentaDAO(cuenta)
    cuentaDAO.mostrar_cuenta()

        
def ver_giros_cuenta():
    print('==== Ver saldos cuenta ====')
    nroCuenta = int(input('Ingrese numero cuenta a revisar giros: '))
    giro = Giro(nroCuenta=nroCuenta)
    giroDAO = GiroDAO(giro)
    giroDAO.mostrar_giros()

def menu_principal():
    while True:
        os.system('cls')
        print('==== Menu de acciones ====')
        print('1. Realizar giro')
        print('2. Ver saldo cuenta')
        print('2. Ver giros cuenta')
        
        opcion = input('Ingrese su opcion: ')
        os.system('cls')
        
        if opcion == '1':
            realizar_giro()
        elif opcion == '2':
            ver_saldos_cuenta()
        elif opcion == '3':
            ver_giros_cuenta()
        elif opcion == '0':
            break
        else:
            print('Opcion ingresada no valida')
        input('Presione enter para continuar...')
        
menu_principal()