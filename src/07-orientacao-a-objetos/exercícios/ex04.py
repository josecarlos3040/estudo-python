""" Exer 04 """

import ex01
import ex02
import ex03

aluno1 = ex01.Aluno('SP3044939', 'José', 'jose@email.com')
aluno2 = ex01.Aluno('SP3044961', 'Amanda', 'amanda@email.com')
projeto1 = ex02.Projeto(
    1, 'Laboratório de Desenvolvimento de Software', 'João Silva')
projeto2 = ex02.Projeto(
    2, 'Laboratório de Desenvolvimento de Software', 'Marcelo Santos')
participacao = ex03.Participacao(1, '29/06', '07/08', aluno1, projeto2)
participacao2 = ex03.Participacao(2, '17/06', '05/01', aluno2, projeto2)
projeto1.add_participacao(participacao)
projeto1.add_participacao(participacao2)
print(projeto1)
projeto1.print_participacao()
