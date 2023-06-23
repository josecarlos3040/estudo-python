""" Exer da aula sobre a moeda """

import moeda107

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda107.metade(p)}')
print(f'O dobro de {p} é {moeda107.dobro(p)}')
print(f'Aumentando 10%, temos {moeda107.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda107.diminuir(p, 13)}')
