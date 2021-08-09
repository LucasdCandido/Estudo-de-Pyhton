n = float(input('Digite uma nota entre 0 e 10: '))
while (n < 0) or (n>10):
    print('Nota invalida, por favor digite uma nota valida!')
    n = float(input('Digite uma nota valida entra 0 e 10: '))
print('Parabéns! A nota {} esta dentro dos parametros!'.format(n))

"""Faça um programa que leia uma nota e valide ela entre 0 e 10
"""