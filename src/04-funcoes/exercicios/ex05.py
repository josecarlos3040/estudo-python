""" Exer 05 """

print("Calculadora IMC")
h = float(input("Entre com a sua altura em metros: "))
kg = float(input("Entre com o seu peso em quilogramas: "))


individuo = {
    'altura': h,
    'peso': kg
}


def calcular_imc(individuo):
    return kg / (h * h)


def obter_classificacao(imc):
    if imc < 18.5:
        return 'Baixo peso.'
    elif imc <= 24.9:
        return 'Peso Normal.'
    elif imc <= 29.9:
        return 'Excesso de peso.'
    elif imc <= 34.9:
        return 'Obesidade de classe 1.'
    elif imc <= 39.9:
        return 'Obesidade de classe 2.'
    else:
        return 'Obesidade de classe 3.'


def situacao_individuo(imc):
    if imc < 18.5:
        return 'Você deve ganhar peso.'
    elif imc <= 24.9:
        return 'Normal'
    else:
        return 'Perder peso'


imc = calcular_imc(individuo)
imc_classificacao = obter_classificacao(imc)
imc_situacao = situacao_individuo(imc)
print(f'Seu imc é: {imc:.2f}')
print('Você está classificado como:', imc_classificacao)
print('Sua situação:', imc_situacao)
