nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('O seu primeiro nome é {}'.format(n[0]))
print('O seu ultimo nome é {}'.format(n[len(n)-1]))



"""Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o ultimo nome separadamente.

EX: Ana Maria de Souza
Primeiro = Ana
Ultimo = Souza"""