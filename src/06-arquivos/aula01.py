""" Aula 01 - Arquivos """

# open("caminho","r")

# Mode
# r - Leitura
# a - Append / incrementar
# - Write / escrita (ele ira limpar o arquivo e começar do zero)
# X - Criar Arquivo
# r+ - Leitura + Escrita

arquivo = open("src/06-arquivos/test3.txt", "r")

# verifica se o arquivo pode ser lido
print(arquivo.readable())

print(arquivo.read())

# Le o arquivo por linha
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

lista = arquivo.readlines()

print(lista)

print(lista[3])

arquivo.write("C\n")
arquivo.write("C++\n")
arquivo.write("Terraform\n")

arquivo.close()


# importa biblicote a para remover arquivos
import os

if os.path.exists("src/06-arquivos/test2.txt"):
    os.remove("src/06-arquivos/test2.txt")
else:
    print("Arquivo não existe")


# remove pasta (so remove se ela estiver vazia)
os.rmdir("src/06-arquivos/nova_pasta")
