numero = int(input('Digite um numero entre 0 a 999: '))
s = 0
cont = 0
while numero < 999:
    s = s + numero
    numero = int(input('Digite um numero entre 0 a 999: '))
    cont += 1
print('Foram digitados {} numeros e a soma deles é {}'.format(cont,s))



'''Crie um programa que leia varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuario digitar o valor 999, que
é a condição de parada. No final, mostre quantos numeros foram
digitados e qual foi a soma entre eles (desconsiderando o flag)'''