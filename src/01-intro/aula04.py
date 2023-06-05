""" Aula 04 - Variáveis, Constantes e Literais """

# Variável container para guardar dados
# inferência de tipo, ele entende com base no que esta sendo passado

numero = 10
print(numero, type(numero))

# alterar o valor de uma variável
numero = 20
print(numero)

# multiplas atribuiçoes / não é uma boa pratica
nome, idade, endereco = 'Maria', 20, 'Rua das  ...'
print(nome, idade, endereco)

# melhor assim
nome = 'Maria'
idade = 20
endereco = 'Rua das ...'
print(nome, idade, endereco)

# atribui o mesmo valor para várias varáveis
nome1 = nome2 = nome3 = 'João'

print(nome1, nome2, nome3)

nome2 = 'Pedro'
print(nome1, nome2, nome3)

# Variáveis
# snake_case
id_funcionario = 209
# clica com botao direito + f2 muda o nome em tudo
salario_atual = 5000.50
print(id_funcionario, salario_atual)

# Constantes
# Sempre em Upper case - snake_case

PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18

print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)


# Literais
idade - 27
print(idade)
print(27)

# Númericos
print(10, type(10))
print(10, type(-10))
print(10.5, type(10.5))

# String
print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("John's house")
print('O filme estava "excelente"')

# aspas unicas ou duplas são a mesma coisa, mas escolha uma e siga ela

# Booleano
print(True, type(True))
print(False, type(False))

# None
print(None, type(None))

# Coleções

# Lista (list) é mutavel
numeros = [1, 3, 5]
print(numeros, type(numeros))

# Tupla (tuple) não mutavel
emails = ('joão@email.com', 'maria@email.com')
print(emails, type(emails))

# Conjunto (set) não permite elementos repetidos e não garante ordens
nomes = {'maria', 'joão', 'pedro', 'maria'}
print(nomes, type(nomes))

# Dicionário (dictionary)
aluno = {
    'prontuario': 123456,
    'nome': 'Maria da Silva',
    'idade':  34
}

print(aluno, type(aluno))
