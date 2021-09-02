cadastro = []
pessoa = []
resposta = ""
media = 0
while True:
    pessoa.append(input('Digite o nome do aluno: ').upper().strip())
    pessoa.append(float(input('Digite a primeira nota do aluno: ')))
    pessoa.append(float(input('Digite a segunda nota do aluno: ')))
    cadastro.append(pessoa[:])
    pessoa.clear()
    resposta = input('Gostaria de cadastrar mais um aluno? [S/N] ').upper().strip()
    if resposta == 'N':
        break
for l in range(0, len(cadastro)):
    media = (l[1] + l[2])/2
    print(l[0], media)
print(cadastro)



"""Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada
aluno individualmente.
"""