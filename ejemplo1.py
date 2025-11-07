# Creando clase
class Empleado:
    # Aca van los atributos
    # 1. Atributos de clase
    direccion = 'Avenida siempre viva 2190'
    
    # 2. Atributos de instancia
    def __init__(self, telefono): # 123456
        self.telefono = telefono
        
# Instancia de clase
e = Empleado(123456)

print(e) # Esto imprime el espacio en memoria del objeto

# Mostrando el telefono del empleado
print(f'El telefono del empleado es {e.telefono}')
# Mostrando direccion del empleado
print(f'La direccion del empleado es {e.direccion}')

e2 = Empleado(99999999)
# Mostrando el telefono del empleado
print(f'El telefono del empleado es {e2.telefono}') #99999999
# Mostrando direccion del empleado
print(f'La direccion del empleado es {e2.direccion}') # 'Avenida siempre viva 2190'

# print(e2.nombre) Esto da error

# Puedes agregar atributos dinamicamente
e2.nombre = 'Perico los Palotes'
print(e2.nombre)
print(e.nombre)