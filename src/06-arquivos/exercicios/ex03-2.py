""" Exer 03 com outra logica """

def linha_para_dict(values_str, keys):
    values = values_str.split(',')

    dictionary = {}
    for i in range(len(keys)):
        if i < len(values):
            dictionary[keys[i]] = values[i]
        else:
            dictionary[keys[i]] = None

    return dictionary


with open("src/06-arquivos/exercicios/valores.txt", "r") as values_file:
    values_str = values_file.read().strip()


with open("src/06-arquivos/exercicios/chaves.txt", "r") as keys_file:
    keys_str = keys_file.read().strip()

keys = keys_str.split(',')

result = linha_para_dict(values_str, keys)

print("{")
for key, value in result.items():
    print(f"    '{key}': '{value}',")
print("}")