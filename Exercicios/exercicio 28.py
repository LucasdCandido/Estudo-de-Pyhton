n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

me = n1
if n2<n3 and n2<n1:
    me = n2
if n3<n1 and n3<n2:
    me = n3
ma = n1
if n2>n3 and n2>n1:
    ma = n2
if n3>n1 and n3>n2:
    ma = n3
    
print('O menor numero é {} e o maior numero é {}.'.format(me,ma))



"""Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor."""