vel = int(input('Qual a velocidade atingida: '))
va = float((vel-80)*7)
av = vel-80

if vel < 80:
    print('Você esta dentro do limite de volocidade permitido!')
else:
    print('Você ultrapassou o limite de velocidade em {}Km/h e a multa vai ser R${:.2f}'.format(av,va))




"""Escreva um programa que leia a velocidade de um carro

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado

A multa vai custar R$7.00 por cada Km acima do limite"""