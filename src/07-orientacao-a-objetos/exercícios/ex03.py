""" Exer 03 """

import ex01
import ex02


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if value <= 0 or not value:
            raise ValueError("Codigo invalido")
        self._codigo = value

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, value):
        if value == " " or not value:
            raise ValueError("Data de inicio invalida")
        self._data_inicio = value

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, value):
        if value == " " or not value:
            raise ValueError("Data fim invalida")
        self._data_fim = value

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __str__(self):
        return f'Participacao: {self.codigo}, data inicio: {self.data_inicio}, data fim: {self.data_fim}, {self.aluno}, {self.projeto}'


aluno1 = ex01.Aluno('SP3044939', 'Jose Carlos',
                    'jose.viveiros@aluno.ifsp.edu.br')
projeto1 = ex02.Projeto(2, 'Acelerador de Particulas', 'José Carlos')
participacao1 = Participacao(1, "05/3/2023", "28/09/2023", aluno1, projeto1)
print(participacao1)
