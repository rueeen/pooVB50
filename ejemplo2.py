class Empleado:
    def __init__(self, nombre:str, telefono:int, direccion:str):
        print('Esto se ejecuta solo cada vez que instancias')
        self.nombre = nombre
        self.direccion = direccion
        self.telefono  = telefono
        
    def __str__(self):
        return f'Datos empleado: {self.nombre} - {self.telefono} - {self.direccion}' 
        
e1 = Empleado('Perico los Palotes', 999999999, 'Av falsa 123')
e2 = Empleado('Maria las Petunias', 88888888, 'Av Paz 666')
e3 = Empleado('Perico los Palotes', 999999999, 'Av falsa 123')

if e1 == e3:
    print('Son iguales')
else:
    print('Son diferentes')
    
if e1.nombre == e3.nombre:
    print('Son iguales')
else:
    print('Son diferentes')
    
nombre = input('Ingrese nombre empleado: ')
telefono = int(input('Ingrese telefono empleado: '))
direccion = input('Ingrese direccion empleado: ')

e4 = Empleado(nombre=nombre, direccion=direccion, telefono=telefono)

print(e4) # 0x034343