from random import randint
from time import sleep

print('''Gostaria de participar de um jogo? Então é só escolher um numero entre
      1 e 10 para poder participar!
      Sera que você consegue acertar o numero que o computador escolheu?
      Vamos ver!!!''')

player = int(input('Digite um numero entre 1 e 10: '))
 
ran = randint(1,10)
pc = ran
cont = 0
while player != pc:
    sleep(1)
    player = int(input('Ainda não foi dessa vez! Tente novamente!: '))
    pc = ran
    cont += 1
sleep(1)
print('Você tentou {} vezes para conseguir descobrir o numero!'.format(cont))
sleep(0.5)
print('Parabéns tanto você quanto o computador escolheram o numero {}!'.format(pc))



'''Melhore o jogo do Desafio 28 onde o computador vai 'pensar' em um numero entre 0
a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessarios para vencer.'''