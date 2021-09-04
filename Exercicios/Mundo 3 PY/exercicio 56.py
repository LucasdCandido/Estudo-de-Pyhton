from random import randint
from time import sleep
from operator import itemgetter
'''partidas = {}
rank = {}
jogos = []
n = 0
partidas['Jogador'] = 'Jogador 1'
partidas['Dado'] = randint(1,6)
jogos.append(partidas.copy())
partidas['Jogador'] = 'Jogador 2'
partidas['Dado'] = randint(1,6)
jogos.append(partidas.copy())
partidas['Jogador'] = 'Jogador 3'
partidas['Dado'] = randint(1,6)
jogos.append(partidas.copy())
partidas['Jogador'] = 'Jogador 4'
partidas['Dado'] = randint(1,6)
jogos.append(partidas.copy())
for c in range(0,4):
    if c == 0 or c['Dado'] < rank[-1]:
        rank.append(c)'''
jogo = { 'Jogador1': randint(1,6),
         'Jogador2': randint(1,6),
         'Jogador3': randint(1,6),
         'Jogador4': randint(1,6)}
ranking = {}
print('Jogos sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)




"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que
o vencedor tirou o maior numero no dado.
"""