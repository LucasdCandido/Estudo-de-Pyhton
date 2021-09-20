num = int(input('Quantos Km você pretende viajar? '))
n1 = num*.5
n2 = num*.45
if num <= 200:
    print('O valor da passagem para {}Km é R${:.2f}'.format(num,float(n1)))
else:
    print('O valor da passagem para {}KM é R${:.2f}'.format(num,float(n2)))



"""Desenvolva um programa que pergunte a dustancia de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até
200Km e R$0.45 para viagens mais longas."""