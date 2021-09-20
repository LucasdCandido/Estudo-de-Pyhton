idade = contador18 = contadorm = contador18f = 0
sexo = escolha = ""
while True:
    idade = int(input('Digite a sua idade: '))
    while idade < 0:
        idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: [M/F] ').upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        contador18 += 1
    if sexo == 'M':
        contadorm += 1
    if idade < 18 and sexo == 'F':
        contador18f += 1
    escolha = str(input('Você gostaria de continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Foram registrados {contadorm} homens, {contador18f} mulheres com menos de 18 anos e {contador18} pessoas com mais de 18 anos.')
print('Esse é o fim do programa!')



"""Crie um programa qe leia a idade e o sexo de varias pessoas.
A cada pessoa cadastrada, o programa devera perguntar se o 
usuario quer ou não continuar. No final mostre:
A) quantas pessoas tem mais de 18 anos.
B) Quantas homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""