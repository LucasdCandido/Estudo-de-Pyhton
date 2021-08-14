from random import randint
computador = jogador = contador = soma = resto = par = impar = resultado = 0
escolha = ""
print('=-='*30)
print('''Vamos jogar par ou impar?
    Você vai competir com o computador, vamos ver quem tem mais sorte! ''')
print('=-='*30)
while True:
    computador = randint(1,10)
    escolha = str(input('Você gostaria de escolher PAR ou IMPAR? ')).upper().strip()
    while escolha not in 'PARIMPAR':
        escolha = str(input('Por favor escolha entre PAR ou IMPAR: '))
    if escolha == 'PAR':
        jogador = int(input('Digite um numero para jogar: '))
        soma = computador + jogador
        resto = soma % 2
        if resto == 0:
            print(f'Parabéns você venceu, você escolheu o numero {jogador} e o computador escolheu o numero {computador} somando da {soma} que é PAR!')
            resultado = 0
            contador += 1
        elif resto != 0:
            print(f'Infelizmente você perdeu, você escolheu {jogador} e o computador escolheu {computador} somando da {soma} que é IMPAR!')
            resultado = 1
    elif escolha == 'IMPAR':
        jogador = int(input('Digite um numero para jogar: '))
        soma = computador + jogador
        resto = soma % 2
        if resto != 0:
            print(f'Parabéns você venceu, você escolheu o numero {jogador} e o computador escolheu o numero {computador} somando da {soma} que é IMPAR!')
            resultado = 0
            contador += 1
        elif resto == 0:
            print(f'Infelizmente você perdeu, você escolheu {jogador} e o computador escolheu {computador} somando da {soma} quie é PAR!')
            resultado = 1
    if resultado == 1:
        break
print(f'Você venceu {contador} vezes!')





"""Faça um programa que jogue par ou impar com o computador.
O jogo só sera interrompido quando o jogador perder, mostrando
o total de vitorias consecutivas que ele conquistou no final do jogo
"""