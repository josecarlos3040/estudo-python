""" Exer 03 """

def linha_para_dict(valores_str, chaves):

    valores = valores_str.split(',')

    dicionario = {}
    for i in range(len(chaves)):
        if i < len(valores):
            dicionario[chaves[i]] = valores[i]
        else:
            dicionario[chaves[i]] = None

    return dicionario


with open("src/06-arquivos/exercicios/valores.txt", "r") as arquivo_valores:
    valores_str = arquivo_valores.read().strip()


with open("src/06-arquivos/exercicios/chaves.txt", "r") as arquivo_chaves:
    chaves_str = arquivo_chaves.read().strip()


chaves = chaves_str.split(',')


dicionario = linha_para_dict(valores_str, chaves)


print("{")
for chave, valor in dicionario.items():
    print(f"    '{chave}': '{valor}',")
print("}")