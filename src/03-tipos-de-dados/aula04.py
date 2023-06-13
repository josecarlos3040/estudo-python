""" Aula 04 - Tipos de Dados - Dicts """

# dict (dicionário)
# colção de key value (chave-valor)
# key ela é única
# mutável

# criação de um dic
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

print(carro, type(carro))


# acessar valores por chave
print(carro["marca"])
print(carro.get("marca"))

# pegar todas as chaves, valores, pares
print(carro.keys())
print(carro.values())
print(carro.items())

# verifica se a chave existe
print("cor" in carro)

# adicionar chave/valor de forma dinâmica
carro["cor"] = 'Azul'
print("cor" in carro)
print(carro, type(carro))

# remove a chave
marca = carro.pop("marca")
print(marca)
print(carro)

# loop
for key in carro:
    print(key, carro[key], type(key))

for value in carro.values():
    print(value)

for key in carro.keys():
    print(key)

print(carro.items())

for key, value in carro.items():
    print(key, value)

# lista de dicionarios

aluno1 = {
    'nome': 'João',
    'email': 'joao@gmail.com',
    'notas': [10, 5, 7]
}

aluno2 = {
    'nome': 'Maria',
    'email': 'maria@gmail.com',
    'notas': [5, 8, 10]
}

alunos = [aluno1, aluno2]

for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(nota)