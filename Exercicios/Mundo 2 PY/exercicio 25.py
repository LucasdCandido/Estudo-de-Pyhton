n = int(input('Digite um numero para calcular o Fatorial: '))
c = n
f = 1
print('Calculando o fatorial de {}.'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = \n', end='')
    f *= c
    c -= 1
print('O fatorial de {} é {}!'.format(n, f))
    




'''Faça um programa que leia um numero qualquer e mostre o seu fatorial
EX:
5! = 5x4x3x2x1=120'''