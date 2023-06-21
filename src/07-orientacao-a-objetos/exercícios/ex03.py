""" Exer 03 """


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if value == " " or not value:
            raise ValueError("Codigo invalido")
        self._codigo = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if value == " " or not value:
            raise ValueError("Titulo invalido")
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if value == " " or not value:
            raise ValueError("Responsavel invalido")
        self._responsavel = value

    @classmethod
    def from_string(cls, rep_projeto):
        codigo, titulo, responsavel = rep_projeto.split(sep=",")
        return cls(codigo, titulo, responsavel)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __str__(self):
        return f'[Projeto: {self.codigo}, {self.titulo}, {self.responsavel}]'


class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if value == " " or not value:
            raise ValueError("Prontuario invalido")
        self._prontuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if value == " " or not value:
            raise ValueError("Nome invalido")
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value == " " or not value:
            raise ValueError("Email invalido")
        self._email = value

    @classmethod
    def from_string(cls, rep_aluno):
        prontuario, nome, email = rep_aluno.split(sep=",")
        return cls(prontuario, nome, email)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)

    def __str__(self):
        return f'[Aluno: {self.prontuario}, {self.nome}, {self.email}]'


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
        return f'Participacao: {self.codigo}, data inicio:{self.data_inicio}, data fim=:{self.data_fim}, {self.aluno}, {self.projeto}'


aluno1 = Aluno('SP3044939', 'Jose Carlos', 'jose.viveiros@aluno.ifsp.edu.br')
projeto1 = Projeto(2, 'Acelerador de Particulas', 'José Carlos')
participacao1 = Participacao(1, "05/3/2023", "28/09/2023", aluno1, projeto1)
print(participacao1)
