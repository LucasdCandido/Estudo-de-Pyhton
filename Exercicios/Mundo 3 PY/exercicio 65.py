from random import randint
from time import sleep

def sorteio(lista):
    for c in range(0,5):
        n = randint(0,10)
        lista.append(n)
        print(f'{n} ',end="", flush=True)
        sleep(0.2)

  


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'\n{soma}')





numeros = []
sorteio(numeros)
somaPar(numeros)



"""
Faça um programa que tenha uma lista chamada numeros e duas funções chamadas
sorteio() e somaPar(). A primeira função vai sortear 5 numeros e vai colocalos
dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterios.
"""