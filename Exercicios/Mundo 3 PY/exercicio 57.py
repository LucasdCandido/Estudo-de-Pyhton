from datetime import datetime
cadastro = {}
cadastros = []
resposta = ""
idade = nascimento = 0

while True:
    cadastro['Nome'] = input('Digite seu nome: ')
    nascimento = int(input('Digite seu ano de nascimento: '))
    idade = datetime.now().year - nascimento
    cadastro['Idade'] = idade
    cadastro['CTPS'] = int(input('Digite o numero da carteira de trabalho: [Caso não tenha carteira de trabalho digite 0] '))
    if cadastro['CTPS'] != 0:
        contratado = int(input('Digite o ano em que começou a trabalhar: '))
        cadastro['Contribui'] = contratado
        cadastro['Salario'] = float(input('Digite seu salario: R$ '))
        contribuicao = 35 - (datetime.today().year - contratado)
        if contribuicao < 0:
            contribuicao = datetime.today().year - contratado
            cadastro['Tempo de contribuição'] = contribuicao
        else:
            cadastro['Tempo Faltante'] = contribuicao
    resposta = input('Gostaria de cadastrar outra pessoa? [S/N] ').upper().strip()[0]
    cadastros.append(cadastro.copy())
    if resposta == 'N':
        break
for c in cadastros:
    print(c)




"""Crie um programa que leia nomes, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um
dicionario se por acado a CTPS for diferente de zero, o dicionario recebera também o ano de contratação e o salario.
Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
35 anos de contribuição
"""