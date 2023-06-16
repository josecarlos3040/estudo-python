""" exer - 01 """

def carregar_dados_alunos(caminho_dados):
    dados_alunos = ()
    with open(caminho_dados, 'r', encoding='utf-8') as dados:
        for linha in dados:
            linha = linha.strip()
            if linha:
                prontuario, nome, email = linha.split(',')
                info_aluno = {
                    'prontuario': prontuario,
                    'nome': nome,
                    'email': email
                }
                dados_alunos += (info_aluno,)
    return dados_alunos

CAMINHO_DADOS = 'src/06-arquivos/exercicios/dados_cadastrados_aluno.txt'
tupla_dados = carregar_dados_alunos(CAMINHO_DADOS)

for aluno in tupla_dados:
    print('{')
    for key, value in aluno.items():
        print(f'    {key}: {value}')
    print('}')