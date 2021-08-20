from random import randint
numero1 = numero2 = numero3 = numero4 = numero5 = random = contador = maior = menor = m = 0
numero1 = randint(1, 10)
numero2 = randint(1, 10)
numero3 = randint(1, 10)
numero4 = randint(1, 10)
numero5 = randint(1, 10)
random = (numero1, numero2, numero3, numero4, numero5)
a, b, c, d, e = random
for c in range(0, len(random), 1):
    m = random[c]
    contador += 1
    if contador == 1:
        maior = menor = m
    else:
        if m > maior:
            maior = m
        if m < menor:
            menor = m
print(f'A sequecia aleatoria ficou {a, b, c, d, e}, o maior numero da sequencia é {maior} e o menor é {menor}.')


"""Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de numeros gerados e também indique o menor e o maior valor que estão na tupla.
"""