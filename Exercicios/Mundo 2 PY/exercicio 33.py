from random import randint
computador = jogador = contador = 0
escolha = ""
par = 0
impar = 0
print('=-='*30)
print('''Vamos jogar par ou impar?
    Você vai competir com o computador, vamos ver quem tem mais sorte! ''')
while True:
    jogador = int(input('Digite o numero para poder jogar par ou impar: '))
    computador = randint(1, 10)
    escolha = str(input('Você quer par ou impar? ')).upper().strip()
    while escolha not in 'PAR' or 'IMPAR':
        escolha = str(input('Você deve escolher entre par ou impar para conseguir jogar: ')).upper().strip()



"""Faça um programa que jogue par ou impar com o computador.
O jogo só sera interrompido quando o jogador perder, mostrando
o total de vitorias consecutivas que ele conquistou no final do jogo
"""