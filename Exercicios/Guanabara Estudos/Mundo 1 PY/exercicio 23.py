import random
num = int(input('Digite um numero entre 0 e 5 para tentar acertar o numero do computador.'))
r = random.randint(0,5)
if r == num:
    print('Parabéns, você acertou o numero!')
else:
    print('Que pena, você errou. O numero certo é {}.'.format(r))



"""Escreva um programa que faça o computador "pensar" em um numeor inteiro
entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo pc

O programa devera escrever na tela se o usuario venceu ou perdeu"""