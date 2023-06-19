""" Aula 01 - Introdução a Orientação a objetos """

# paradigma de programação

# calcular a área de o perimetro de um retangulo
# area = base * altura
# perímetro = 2 * (base + altura)
# estrutura para armazenar os valores necessários para os calculos

retangulo1 = {
    'base': 10.0,
    'altura': 5.0
}

retangulo2 = {
    'base': 6.0,
    'altura': 3.0
}

# Realizar os cálculos


def caalcular_area(retangulo):
    return retangulo['base'] * retangulo['altura']


def caalcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])

print(caalcular_area(retangulo1))
print(caalcular_area(retangulo2))

print(caalcular_perimetro(retangulo1))
print(caalcular_perimetro(retangulo2))


# Classe representa um conceito
# Classe representa um retangulo
# Classe possui atributos: baase e altura
# Classe possui métodos
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def caalcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 *(self.base + self.altura)

# instanciando objetos do tipo Retangulo
# Chammando o método construtor
retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(5.0, 3.0)



print(type(retangulo1), retangulo1)
print(type(retangulo2), retangulo2)

print(retangulo1.base,
    retangulo1.altura, 
    retangulo1.caalcular_area(),
    retangulo1.calcular_perimetro()
)

print(retangulo2.base,
    retangulo2.altura, 
    retangulo2.caalcular_area(),
    retangulo2.calcular_perimetro()
)
