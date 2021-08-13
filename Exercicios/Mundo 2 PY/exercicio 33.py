from random import randint
computador = jogador = contador = soma = resto = 0
escolha = ""
par = 0
impar = 0
resultado = 0
print('=-='*30)
print('''Vamos jogar par ou impar?
    Você vai competir com o computador, vamos ver quem tem mais sorte! ''')
while True:
    computador = randint(1,10)
    escolha = str(input('Você gostaria de escolher PAR ou IMPAR? ')).upper().strip()
    while escolha not in 'PAR' or 'IMPAR':
        escolha = str(input('Por favor escolha entre PAR ou IMPAR: '))
    if escolha == 'PAR':
        jogador = int(input('Digite um numero para jogar: '))
        soma = computador + jogador
        contador += 1
        resto = soma % 2
        if resto == 0:
            





"""Faça um programa que jogue par ou impar com o computador.
O jogo só sera interrompido quando o jogador perder, mostrando
o total de vitorias consecutivas que ele conquistou no final do jogo
"""