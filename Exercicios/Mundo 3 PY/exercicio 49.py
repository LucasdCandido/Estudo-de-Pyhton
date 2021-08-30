cadastro = []
pessoa = []
maior = menor = 0
resposta = ""
while True:
    pessoa.append(input('Digite seu nome: ').upper().strip())
    pessoa.append(float(input('Digite seu peso: ')))
    if len(cadastro) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    cadastro.append(pessoa[:])
    pessoa.clear()
    resposta = input('Gostaria de cadastrar mais uma pessoa? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
for c in cadastro:
    if c[1] == maior:
        print(c[0], c[1])
    if c[1] == menor:
        print(c[0], c[1])
print(len(cadastro))



"""Faça um programa que leia o nome e o peso de varias pessoas, guardando tudo em uma lista. no final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma lista com as pessoas mais pesadas.
C) Uma lista com as pessoas mais leves.
"""