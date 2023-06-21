""" Aula 08 - Herança entre Classes """


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

    def calcula_pagamento(self):
        return self.salario - ((10/100) * self.salario)


class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcula_pagamento(self):
        pagamento_salario = super().calcula_pagamento()
        return pagamento_salario + self.bonus


programador = Programador("Arthur", "Melo", '123.123.123-12', 4800, 200)
print(programador.nome_completo())
print(programador.calcula_pagamento())

funcionario = Funcionario("Amanda", "Maria", '123.123.123-12', 5000)
print(funcionario.nome_completo())
print(funcionario.calcula_pagamento())


cliente = Cliente("José", "Carlos", '123.123.123-12')
print(cliente.nome_completo())
