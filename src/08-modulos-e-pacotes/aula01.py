""" Aula 01 - Modulos e pacotes """

from uteis import numeros
# import uteis

num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
