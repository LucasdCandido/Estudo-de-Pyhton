from random import randint
from time import sleep
'''dicas = []
jogos = []
contador = resposta = jogo = 0
resposta = int(input('Quantos jogos gostaria de fazer? '))
while True:
    for l in range(0,resposta):
        for c in range(0,6):
            jogos.append(randint(1,60))
        jogos.sort()
        dicas.append(jogos[:])
        jogos.clear()
    contador += 1
    if contador < resposta:
        break
for l in range(0,len(dicas)):
    print(dicas[l])'''
jogos = []
dicas = []
resposta = int(input('Quantos jogos quer fazer? '))
total = 1
while total <= resposta:
    total += 1
    contador = 0
    while True:
        num = randint(1,60)
        if num not in jogos:
            jogos.append(num)
            contador += 1
        if contador >= 6:
            break
    jogos.sort()
    dicas.append(jogos[:])
    jogos.clear()
for i, l in enumerate(dicas):
    print(l)
    sleep(1)


"""Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 numeros entre 1 a 60 para cada jogo, cadastrando tudo em uma lista
composta.
"""