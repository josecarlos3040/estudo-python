""" Aula 02 - Atributos de classe e instancia """


# classe pessoa possui
# atributos de instancia: nome e email
# atributos de classe: especie
class Pessoa:
    especie = 'Humano'

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


pessoa1 = Pessoa('Mariaa da Silva', 'maria@email.com')
pessoa2 = Pessoa('João da Silva', 'joao@email.com')
pessoa3 = Pessoa('Pedro da Silva', 'pedro@email.com')

# alterar um atributo de classe na instancia (objeto)
# altera somente para aquela instancia
pessoa1.especie = 'Alienigena'

# alterando um atributo de classe na calsse
# altera todos os objetos e na classe também
Pessoa.especie = "Alienigenas do Passado"

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print(pessoa3.nome, pessoa3.email, pessoa3.especie)
print(Pessoa.especie)
