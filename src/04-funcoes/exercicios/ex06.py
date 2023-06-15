""" Exer 06 """

print("Calculador aquário")
comprimento = float(input("Entre com o comprimento do aquário: "))
altura = float(input("Entre com a altura do aquário: "))
largura = float(input("Entre com a largura do aquário: "))

temperatura_desejada = float(input("Entre com a temperatura desejada: "))
temperatura_ambiente = float(input("Entre com a temperatura ambiente: "))


def calcular_volume(comprimento, altura, largura):
    return comprimento * altura * largura / 1000


def potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)


def filtragem_hora(volume):
    filtragem1 = volume * 2

    return f'A filtragem por hora deve ser de {filtragem1} em {filtragem1} hora'


volume = calcular_volume(comprimento, altura, largura)
print('O volume do aquário é', volume)

potencia = potencia_termostato(
    volume, temperatura_desejada, temperatura_ambiente)
print('A potência ideal do termostato é:', potencia)

filtragem = filtragem_hora(volume)
print(filtragem)
