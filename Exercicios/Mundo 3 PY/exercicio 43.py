valores = []
maior = menor = contador = 0
while contador < 0:
    valores.append(int(input('Digite um numero: ')))
for v in valores:
    if v in valores:
        maior = menor = v
    else:
        if maior < v:
            maior = v
        if menor > v:
            menor = v
if menor in valores:
    print(valores.index(menor))
if maior in valores:
    print(valores.index(maior))



"""Faça um programa que leia 5 valores numericos e guardeos em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""