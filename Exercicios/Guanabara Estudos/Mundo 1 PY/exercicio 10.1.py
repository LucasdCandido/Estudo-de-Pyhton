from math import sqrt

def raiz(numero):
    print(f'O numero {numero} tem a raiz {sqrt(numero):.2f}')

numero = int(input('Digite um numero: '))
raiz(numero)