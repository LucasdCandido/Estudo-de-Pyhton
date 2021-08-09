from datetime import date
from time import sleep
print("""Sejam todos muito bem vindos! Vamos começar aqui a seleção e classificação dos nadadores!
      Vamos classificar de acordo com o ano de nascimento dos competidores sendo classificado como:
      Até 9 anos de idade como Mirim!
      Até 14 anos de idade como Infantil!
      Até 19 anos de idade como Junior!
      Até 20 anos de idade como Senior!
      E todos acima disso como Master!
      Boa sorte a todos!!!""")
sleep(2)
nome = str(input('Olá, qual o seu nome: '))
print('Seja bem vindo(a) {}!'.format(nome))
sleep(0.5)
idade = int(input('Qual o ano de nascimento do competidor: '))
sleep(0.5)
print('-'*5)
sleep(0.5)
print('-'*10)
sleep(0.5)
print('Estamos verificando nossos bancos de dados só um momento por favor')
sleep(0.5)
print('-'*15)
sleep(0.5)
print('-'*20)
sleep(0.5)
print('Pronto esse é o resultado!')
sleep(0.5)
atual = date.today().year
id = atual-idade
if id<9:
    print('Parabéns pela inscrição {}!!! Você vai participar da categoria Mirim!'.format(nome))
elif id<14:
    print('Parabéns pela inscrição {}!!! Você vai participar da categoria Infantil'.format(nome))
elif id<19:
    print('Parabéns pela inscrição {}!!! Você vai participar da categoria Junior!'.format(nome))
elif id<20:
    print('Parabéns pela inscrição {}!!! Você vai participar da categoria Senior!'.format(nome))
else:
    print('Parabéns pela inscrição {}!!! Você vai participar da categoria Mestre!'.format(nome))



"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: Mirim
-Até 14 anos: Infantil
-Até 19 anos: Junior
-Até 20 anos: Senior
-Acima: Master"""