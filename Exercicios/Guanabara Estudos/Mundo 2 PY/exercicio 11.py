import emoji
from time import sleep
for item in range(10, -1, -1):
    print('Contagem regressiva para lançar os fogos começando em {}'.format(item))
    sleep(1)
print(emoji.emojize('LANÇAR :fireworks:'))


"""Faça um programa que mostre na tela uma 
contagem regressiva para o estouro de fogos
de artificio, indo de 10 até 0, com uma pausa
de 1 segundo entre elas"""