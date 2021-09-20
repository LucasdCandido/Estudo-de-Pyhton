'''cadastro = []
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
    media = sum(l[1] + l[2])/2
    print(l[0], media)
print(cadastro)
'''
cadastro = []
while True:
    nome = input('Digite o seu nome: ').strip()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    cadastro.append([nome, [nota1, nota2], media])
    resposta = input('Gostaria de cadastrar outro aluno? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break

print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(cadastro):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    notas = int(input('Qual aluno gostaria de ver as notas?  (999 interrompe): '))
    if notas == 999:
        break
    if notas <= len(cadastro) -1:
        print(f'Notas de {cadastro[notas][0]} são {cadastro[notas][1]}')
        
    


"""Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada
aluno individualmente.
"""