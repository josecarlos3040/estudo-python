""" Ex 01 """

num1 = float(input('Entre com o primeiro numero: '))
num2 = float(input('Entre com o segundo numero: '))
num3 = float(input('Entre com o terceiro numero: '))

lista = [num1, num2, num3]

menor = lista[0]
maior = lista[0]

for num in lista:
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print("Menor número:", menor)
print("Maior número:", maior)