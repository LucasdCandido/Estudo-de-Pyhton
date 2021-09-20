'''pessoa = {}
cadastro = []
mulheres = []
nome = sexo = ""
idade = media = idades = 0
while True:
    pessoa['Nome'] = input('Digite seu nome: ').strip().upper()
    idade = int(input('Digite sua idade: '))
    idades += idade
    pessoa['Idade'] = idade
    while True:
        pessoa['Sexo'] = input('Digite seu sexo: [M/F] ').upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Por favor, digitar apenas M ou F')
    cadastro.append(pessoa.copy())
    resposta = input('Gostaria de cadastrar outra pessoa? [S/N] ').upper().strip()[0]
    if resposta in 'N':
        break
media = idades/len(cadastro)
print(f'A media de idade das pessoas cadastradas é {media:.0f}')
for c in cadastro:
    for l in c:
        if l == 'F':
            mulheres.append()
print(mulheres)'''
galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = input('Nome: ').upper().strip()
    while True:
        pessoa['Sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Por favor, digitar apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resposta = input('Quer continuar? [S/N] ').upper().strip()[0]
        if resposta in 'SN':
            break
        print('Responda apenas S ou N.')
    if resposta == 'N':
        break
print(len(galera))
media = soma / len(galera)
print(media)
for c in galera:
    if c['Sexo'] in 'Ff':
        print(c["Nome"])
for c in galera:
    if c['Idade'] >= media:
        for k, v in c.items():
            print(k,v)


"""Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados
de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A media de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da media
"""