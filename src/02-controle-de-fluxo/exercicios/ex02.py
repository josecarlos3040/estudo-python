""" Ex 02 """

notas = input("Digite as 3 notas (separe as notas): ")
notas_list = notas.split(",")

n1 = float(notas_list[0].strip())
n2 = float(notas_list[1].strip())
n3 = float(notas_list[2].strip())

NOTA1_VALIDA = 0 <= n1 <= 10
NOTA2_VALIDA = 0 <= n2 <= 10
NOTA3_VALIDA = 0 <= n3 <= 10

if NOTA1_VALIDA and NOTA2_VALIDA and NOTA3_VALIDA:
    media = (n1 + n2 + n3) / 3
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('Notas inválidas')