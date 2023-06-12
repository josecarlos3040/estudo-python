identificador = input("Entre com o identificador de funcionário: ")

erros = []

if len(identificador) == 7:
    if 'BR' not in identificador:
        erros.append("Identificador não inicia com a sequência 'BR'")
    if 'X' not in identificador:
        erros.append("Identificador não finaliza com o caractere 'X'")
    numero = int(identificador[2:6])
    if not (1 <= numero <= 9999):
        erros.append("Identificador não apresenta números inteiros entre 0001 e 9999")
else:
    erros.append("Identificador deve ter 7 caracteres")

if erros:
    print("Erros encontrados:")
    for erro in erros:
        print("-", erro)
else:
    print("Identificador válido")