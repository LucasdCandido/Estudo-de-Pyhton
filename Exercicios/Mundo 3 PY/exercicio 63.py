def contador(inicio, fim, passo):
    for c in range(1, 11, 1):
        print(f'{c} ',end="")
    print()
    for c in range(10, 0, -2):
        print(f'{c} ',end="")
    print()
    for c in range(inicio, fim, passo):
        print(f'{c} ',end="")


inicio = int(input('Digite o inicio da contagem: '))
fim = int(input('Digite o fim da contagem: '))
passo = int(input('Digite o passo da contagem: '))
if passo == 0:
    passo = 1
if inicio > fim:
    passo = passo *-1
contador(inicio, fim, passo)



"""
Faça um programa que tenha uma função chamada contador(), que receba tres parametros:
inicio, fim e passo e realize a contagem. 
seu programa tem que realizar tres contagens atravez da função criada:
A) de 1 até 10. de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada. 
"""