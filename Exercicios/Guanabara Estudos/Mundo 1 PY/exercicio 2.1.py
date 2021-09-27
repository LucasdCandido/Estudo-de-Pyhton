#aqui temos o caso da necessidade usar uma biblioteca, importamos sqrt que trabalha com raiz de numeros inteiros da biblioteca math que tem varias funcionalidades de matematica
from math import sqrt

def calculo(n):
    dobro = n*2
    triplo = n*3
    raiz = sqrt(n)
    print(f'O valor {n} tem o dobro {dobro}, o triplo {triplo} e a raiz {raiz}')

n = int(input('Digite um numero: '))
calculo(n)