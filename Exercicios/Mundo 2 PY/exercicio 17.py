

for c in range(0, 5):
    i = int(input('Digite um numero para saber se ele é Primo ou não: '))
    if i % 1 == 0 and i % i == 0 and i % 2 != 0 and i % 5 != 0 or 2 or 5:
        print('O numero {} é Primo'.format(i))
    else:
        print('Esse numero {} não é Primo'.format(i))



"""Faça um programa que leia um numero inteiro e
diga se ele é ou não um numero primo"""