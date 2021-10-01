from math import hypot

def hipotenuza(x, y):
    print(f'A soma do quadrado do cateto adjacente {x} mais a soma do quadrado do cateto oposto {y} é igual ao quadrado do cateto da hipotenusa {hypot(x,y):.2f}')


for c in range(3):
    x = int(input('Digite o valor do quadrado do cateto adjacente: '))
    y = int(input('Digite o valor do quadrado do cateto oposto: '))
    hipotenuza(x, y)