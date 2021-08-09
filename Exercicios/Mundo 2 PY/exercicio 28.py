n = int(input('Quantos numeros da sequencia de Fibonacci você gostaria de ver? '))
t1 = 0
t2 = 1
cont = 3
print('{} - {} '.format(t1,t2),end="")
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3),end="")
    t1 = t2
    t2 = t3
    cont += 1
print(' - Fim')




'''Escreva um programa que leia um numero N inteiro qualquer
e mostre na tela os N primeiros elementos de uma sequencia de 
Fibonacci
Ex:
0>1>1>2>3>5>8'''