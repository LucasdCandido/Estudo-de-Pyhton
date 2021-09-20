from time import sleep 

def maior(* numero):
    contador = maior = 0
    print(f'\nAnalizando dados: ')
    for c in numero:
        print(f'{c} ', end='', flush=True)
        sleep(0.3)
        if contador == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        contador += 1
    print(f'\nForam contados {contador} numeros')
    print(f'O maios numero é {maior}')

maior(1,2,3,4,5,6,12)
maior(12,32,99,12)
maior(0)


"""
Faça um programa que tenha uma função chamada maior(), que receba varios parametros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""