valores = []
maior = menor = contador = 0
for c in range(0,5):
    valores.append(int(input('Digite um numero: ')))
for v in valores:
    contador += 1
    if contador == 1:
        maior = menor = v
    else:
        if maior < v:
            maior = v
        if menor > v:
            menor = v
if menor in valores:
    print(f'O menor valor {menor} aparece na posição {valores.index(menor)+1}')
if maior in valores:
    print(f'O maior valor {maior} aparece na posição {valores.index(maior)+1}')



"""Faça um programa que leia 5 valores numericos e guardeos em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""