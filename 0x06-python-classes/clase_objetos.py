"""
Clases: es un contenedor o molde como por ejemplo cuando pensamos en la palabra CARRO
tenemos una imagen mental de un molde de un carro (con llantas, ventanas, etc)
caracteristicascomunes.
Atributos: son caracteristcas especifica, de un carro, por ejemplo la marca, modelo o
la placa
Objetos: en Python todo es un objeto, todas las variables, funciones , listas etc.
"""


from html.entities import name2codepoint


class Carro:
    #en la clase carro creamos 3 objetos:
    marca = ""
    modelo = 0
    placa = ""
#creo un objeto:
taxi = Carro()
#para visualizar los atributos
print(taxi.modelo)


#clase vacia:
class nombre:
    pass

#normalmente los objetos de la clase los ponemos despues:
victor = nombre()
maria = nombre()
#ahora neceitamos crear los atributos:
#objeto.atributo = valor
victor.edad = 21
victor.sexo = "masculino"
victor.pais = "Colombia"
#para visualizar los atributos creados
print(victor.edad)


#Metodos: es una funcion pero esta dentro de una clase por eso de llama asi y no funcion
#self es como nos referimos al objeto
# utilizar self.nombre_de_variable = ALGORITMO

class Matematicas:
#creo un metodo:
    def suma(self): #self hace referencia a un objeto q aun no hemos creado
        self.n1 = 2
        self.n2 = 5
s = Matematicas()
s.suma()
print(s.n1 + s.n2)

#METODOS: __init__   El objetivo fundamental del método 
# es inicializar los atributos del objeto que creamos.

class ropa:
    def __init__(self):
        self.marca = "shannel"
        self.talla = "M"
        self.color = "rojo"
camisa = ropa()
print(camisa.talla) #gracias a __init__ se puede acceder a los atributos mucho mas facil


#ejemplo gasnter:

class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2

operacion = Calculadora(2, 3) #asignamos n1 y n2
print(operacion.suma)
print(operacion.resta)
print(operacion.producto)

