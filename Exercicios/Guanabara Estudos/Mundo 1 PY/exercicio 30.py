r1 = int(input('Digite uma das retas do triangulo: '))
r2 = int(input('Digite uma das retas do triangulo: '))
r3 = int(input('Digite uma das retas do triangulo: '))

if r1<(r2+r3) and r2<(r3+r1) and r3<(r1+r2):
    print('\033[4;30;41m Medidas conseguem formar um triangulo.\033[m')
else:
    print('Medidas precisam ser mudadas, não conseguem montar um triangulo.')



"""Desenvolva um programa que leia o comprimento de tres retas e dia 
ao usuario se elas podem ou não formar um triangulo."""