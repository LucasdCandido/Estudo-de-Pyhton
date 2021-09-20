tabuada = numero = cont = 0
while True:
    numero = int(input('Digite um numero para ver a tabuada: '))
    if numero < 0:
        break
    while True:
        cont += 1
        print(f'{numero} x {cont} = {numero*cont}')
        if cont>=10:
            break
    cont = 0
print('FIM')



"""Faça um programa que mostre a tabuada de varios numeros, um de cada vez,
para cada valor digitado pelo usuario. O programa sera interrompido quando
o numero solicitado for negativo.
"""