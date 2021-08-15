nome = sexo = escolha = ""
idade = letra = 0
cadastro = []

while True:
    nome = str(input('Digite seu nome: ')).upper().strip()
    letra =len(nome)
    while letra < 3:
        nome = str(input('Por favor, digite um nome maior que 3 letras: '))
        letra = len(nome)
    idade = int(input('Digite sua idade: '))
    while idade < 0:
        idade = int(input('Digite um valor valido de idade: '))
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Por favor digite um sexo valido: [M/F] ')).upper().strip()[0]
    cadastro = [nome, idade, sexo]
    escolha = str(input('Gostaria de cadastrar outra pessoa? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break

print(cadastros)







"""Crie um programa qe leia a idade e o sexo de varias pessoas.
A cada pessoa cadastrada, o programa devera perguntar se o 
usuario quer ou não continuar. No final mostre:
A) quantas pessoas tem mais de 18 anos.
B) Quantas homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""