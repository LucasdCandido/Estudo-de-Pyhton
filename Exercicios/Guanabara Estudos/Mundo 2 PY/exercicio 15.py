
s = 0
for c in range(0, 6):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 != 0:
        s = s + num
print('A soma dos numeros impares é {}'.format(s)) 



"""Desenvolva um programa que leia seis numeros
inteiros e mostre a soma apenas daqueles que 
forem pares. Se o valor digitado for impar, 
desconsidere-o"""