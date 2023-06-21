""" Aula 07 - Relacionamentos entre classes """


class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f'Endereco[cep={self.cep}, numero={self.numero}]'


class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f'Telefone[ddd={self.ddd}, numero={self.numero}]'


class Pessoa:
    def __init__(self, cpf, nome, telefone, endereco):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = [endereco]

    def add_endereco(self, endereco):
        self.enderecos.append(endereco)

    def print_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone={self.telefone}]'


telefone = Telefone('11', '11111-11111')
pessoa1 = Pessoa('12345678', 'João da Silva',
                 telefone, Endereco('02345123', 123))
pessoa1.add_endereco(Endereco('02345123', 53))


pessoa2 = Pessoa('123454234', 'Maria da Silva',
                 telefone, Endereco('02678123', 133))


pessoa3 = Pessoa('13333334', 'Pedro', telefone,  Endereco('02678123', 133))

print(pessoa1)
print(pessoa1.cpf, pessoa1.nome, pessoa1.telefone)
print(pessoa1.telefone.ddd, pessoa1.telefone.numero)
print(pessoa2)
print(pessoa2.cpf, pessoa2.nome, pessoa2.telefone)
print(pessoa2.telefone.ddd, pessoa2.telefone.numero)


pessoa1.print_enderecos()
pessoa2.print_enderecos()
pessoa3.print_enderecos()
