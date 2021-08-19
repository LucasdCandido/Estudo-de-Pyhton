numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    print(numero[n])
    resposta = input('Gostaria de digitar mais um numero? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
print('Fim do programa!')



"""Crie um programa que tenha uma tupla totalmente preenchida com
contagem por extrenso, de zero até vinte.
Seu programa devera ler um numero pelo teclado (entre 0 e 20) e 
mostra-lo por extenso.
"""