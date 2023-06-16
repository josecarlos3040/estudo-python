""" Aula 02 - Arquivos """

# arq = open('src/06-arquivos/arquivo.txt', 'w')

# # string = "Ola tudo bem"
# x = ['joão', 'caio', 'marcos']

# for nome in x:
#     arq.write(nome + '\n')

# #arq.write('Caio\nMarcos\nJoão')
# #arq.writelines(x)

# arq.close()


# with open('src/06-arquivos/arquivo.txt', 'rb') as arq: deixa em bytes
with open('src/06-arquivos/arquivo.txt', 'r') as arq:
#    x=arq.read()
#    print(x, type(x))
    print(next(arq))
    print(next(arq))
    for i in arq:
        print(i)

