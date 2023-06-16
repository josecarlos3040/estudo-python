""" exer - 02 """

def carregar_dados_projetos(caminho_dados):
    dados_projetos = ()
    with open(caminho_dados, 'r', encoding='utf-8') as dados:
        for linha in dados:
            linha = linha.strip()
            if linha:
                codigo, titulo, responsavel = linha.split(',')
                info_projetos = {
                    'codigo': codigo,
                    'titulo': titulo,
                    'responsavel': responsavel
                }
                dados_projetos += (info_projetos,)
    return dados_projetos

CAMINHO_DADOS = 'src/06-arquivos/exercicios/dados_cadastrados_projetos.txt'
tupla_dados = carregar_dados_projetos(CAMINHO_DADOS)

for aluno in tupla_dados:
    print('{')
    for key, value in aluno.items():
        print(f'    {key}: {value}')
    print('}')