""" Exer 02 """

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
        return f'Aluno[prontuario={self.codigo}, nome={self.titulo}, email={self.responsavel}]'
    
projeto1 = Projeto(2, 'Acelerador de Particulas', 'José Carlos')
projeto2 = Projeto(1, 'Usina Nuclear', 'Amanda Maria')
print(projeto1)
print(projeto2)