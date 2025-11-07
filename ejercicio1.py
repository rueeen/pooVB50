class Rectangulo:
    def __init__(self, alto:float, largo:float):
        self.__alto = alto
        self.__largo = largo
    
    def calcular_area(self) -> float: # Que el metodo retorna un flotante
        return self.__alto * self.__largo
    
    def calcular_perimetro(self) -> str:
        print(f'El perimetro del rectangulo es { 2* (self.__alto + self.__largo)}')
    
    def obtener_alto(self) -> float:
        return self.__alto
    
    def obtener_largo(self) -> float:
        return self.__largo
    
    def establecer_alto(self, nuevo_valor: float) -> None:
        self.__alto = nuevo_valor
        
    def establecer_largo(self, nuevo_valor: float) -> None:
        self.__largo = nuevo_valor
        
alto = float(input('Ingrese alto: '))
largo = float(input('Ingrese largo: '))
r = Rectangulo(alto=alto, largo=largo)

print(f'El area del rectangulo es: {r.calcular_area()}')
r.calcular_perimetro()
print(f'El alto del rectangulo es: {r.obtener_alto()}')
print(f'El largo del rectangulo es: {r.obtener_largo()}')
nuevo_alto = float(input('Ingrese nuevo alto: '))

r.establecer_alto(nuevo_valor=nuevo_alto)
nuevo_largo = float(input('Ingrese nuevo largo: '))
r.establecer_largo(nuevo_valor=nuevo_largo)
print(f'El area del rectangulo es: {r.calcular_area()}')
r.calcular_perimetro()
print(f'El alto del rectangulo es: {r.obtener_alto()}')
print(f'El largo del rectangulo es: {r.obtener_largo()}')