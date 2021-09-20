from random import randint
from time import sleep
ran = randint(1,3)
r = ran
if r==1:
	r='Pedra'
elif r==2:
	r='Papel'
else:
	r='Tesoura'
jog = int(input("""Ola, seja bem vindo!
Vamos jogar Pedra, Papel e Tesoura?
Funciona da seguinte forma:
	Você vai escolher um numero entre
	1 até 3, sendo Pedra 1, Papel 2 e
	Tesoura 3.
	O Computador também vai
	escolher entre esses três.
	Lembrando que, Pedra ganha de Tesoura mas perde para papel, Papel ganha de Pedra mas perde de Tesoura e Tesoura ganha de papel mas perde de pedra.
Pronto pra jogar? Então escolha um numero entre 1, 2 ou 3: """))
j=jog
if j == 1:
	j = 'Pedra'
elif j==2:
	j = 'Papel'
else:
	j = 'Tesoura'
print('Então você decidiu por {}, muito bem o Computador vai escolher agora!'.format(j))
sleep(3)
print('='*40)
print('PROCESSANDO...')
print('='*40)
if (jog == 1 and ran ==1) or (jog == 2 and ran == 2) or (jog == 3 and ran == 3):
	print('Que pena, você e o Computador escolheram {} então ficou empatado'.format(j))
elif (jog == 1 and ran == 2) or (jog == 2 and ran == 3) or (jog == 3 and ran == 1):
	print('Que pena, você escolheu {} enquanto o Computador escolheu {} então dessa vez quem venceu foi o Computador!'.format(j, r))
else:
	print('Parabéns, você escolheu {} e o Computador {} então dessa vez foi sua sorte e a vitoria é sua!'.format(j, r))
"""Crie um programa que faça o computador jogar jokenpo com você"""