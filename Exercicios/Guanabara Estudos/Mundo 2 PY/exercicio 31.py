soma = cont = numero = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'Foram digitados {cont} numeros e a soma deles é {soma}')





"""Crie um programa que leia varios numero inteiros pelo teclado.
O programa só vai parar quando o usuario digitar o valor 999, que
é a condição de parada. No final, mostre quantos numeros foram 
digitados e qual foi a soma entre eles (desconsiderando o flag)
"""