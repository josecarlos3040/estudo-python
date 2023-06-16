""" Exer 03 - """

def linha_para_dict(chaves, dados):
    dados = dados.strip().split(sep=',')

    dictionary = {}

    for i in range(len(chaves)):
        dictionary[chaves[i]] = dados[i]

    return dictionary

def buscar_dados(nome_arquivo):
    linhas = []
    chaves = []
    valores = ''

    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        for line in file:
            linhas.append(line)
        chaves = linhas[1].strip().split(sep=',')
        valores = linhas[0]

    return chaves, valores

keys, data = buscar_dados('src/06-arquivos/exercicios/dados_exer03.txt')
result = linha_para_dict(keys, data)

print('{')
for key, value in result.items():
    print(f'    {key} : {value}')
print('}')