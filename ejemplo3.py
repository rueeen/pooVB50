class Perro:
    def __init__(self, nombre, raza, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        
    # get y set
    # definiendo un get
    @property
    def nombre(self):
        return self.__nombre
    # definiendo set
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    def ladrar(self):
        print(f'El perro {self.__nombre} esta ladrando')
        
p = Perro('Will', 'Poodle', 3)

p.ladrar()

print(f'El nombre del perro es: {p.nombre}')

p.nombre = 'Silvestre'
print(f'El nombre del perro es: {p.nombre}')