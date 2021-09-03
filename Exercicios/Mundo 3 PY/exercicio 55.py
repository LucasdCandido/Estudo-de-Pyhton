aluno = {}
cadastro = []
while True:
    aluno['Nome'] = input('Digite o nome do aluno: ').strip().upper()
    aluno['Nota1'] = float(input('Digite a primeira nota do aluno: '))
    aluno['Nota2'] = float(input('Digite a seunga nota do aluno: '))
    aluno['Media'] = (aluno['Nota1'] + aluno['Nota2']) / 2
    cadastro.append(aluno.copy())
    resposta = input('Gostaria de cadastrar outro aluno? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
for c in cadastro:
    print(c)
    print()



"""Faça um programa que leia o nome e media de um aluno, guardando também a situação em um dicionario.
No final, mostre o conteudo da estrutura na tela.
"""