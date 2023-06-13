""" Aula 01 - Tipos de dados - Listas """

# Lists
# ordenadas
# mutáveis
# indexáveis

# criação da lista
nomes = ['Maria', 'Pedro', 'João', 1, True]
print(nomes, type(nomes))

print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos
nomes[0] = 'Maria da Silva'

nomes[1:] = ['Pedro da Silva', 'João Santos']
print(nomes)

# tamanho de um lista
# função len
tamanho = len(nomes)
print(len(nomes))

# adicionar elementos na lista
# método append
nomes.append('Marta Gomes')
print(nomes)


# método insert
# coloca na posição e descloca os outros
nomes.insert(0, 'Guilherme Tavares')
print(nomes)

nomes.insert(2, 'Ana lucia')
print(nomes)

# método extend
nomes2 = ['Kaio Silva', 'Carlos Gomes']
print(len(nomes))
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# remover elementos

# método remove

nomes.remove('Maria da Silva')
print(nomes)

# del
del nomes[0]
print(nomes)

# remove da memória
# del nomes
print(nomes)

# limpar a lista
# método clear
# nomes.clear()
print(nomes)

# iteração em lista
for nome in nomes:
    print(nome)


print('----------')
for i in range(len(nomes)):
    print(nomes[i])
