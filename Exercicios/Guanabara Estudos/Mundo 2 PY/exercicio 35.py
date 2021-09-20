soma = preco = n = menor = contador = 0
produto = opcao = produtobarato = ""
while True:
    produto = input('Qual o produto que você gostaria de comprar? ').upper().strip()
    n = len(produto)
    while n < 3:
        produto = input('Qual o produto que você gostaria de comprar? ').upper().strip()
        n = len(produto)
    preco = float(input('Qual o valor do produto? R$ '))
    while preco < 0:
        preco = float(input('Qual o valor do produto? R$ '))
    soma += preco
    if menor > preco:
        produtobarato = produto
    if preco > 1000:
        contador += 1
    opcao = input('Você gostaria de contiuar? [S/N] ').upper().strip()[0]
    if opcao not in 'S':
        break
print(f'O tota da sua compra foi {soma}, {contador} produtos custaram mais que R$ 1000.00 e o produto mais barato foi {produtobarato}')



"""Crie um programa que leia o nome e o preço de varios produtos.
O programa devera perguuntar se o usurario vai continuar. No final mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Quual é o nome do produto mais barato.
"""