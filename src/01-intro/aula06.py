""" Aula 06 - Conversão de Tipos """

# Conversão de tipo implícita e explícita


# Conversao implícita
leitura = 5.53
peso = 3
total = leitura * peso
print(total, type(total))

# Conversao explícita (type casting)
soma = 13.4 + float('3.5')
# soma = 13.4 + float('abc') # Error
print(soma, type(soma))

idade = int('32')
print(idade, type(idade))

nome = "Maria"
altura = 1.70

mensagem = f'{nome} tem a altura de {altura}'
# mensagem = nome + ' tem a altura de ' + str(altura)
print(mensagem)
