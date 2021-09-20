from datetime import date
ano = date.today().year
maior = 0
menor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}ª você nasceu? '.format(pess)))
    idade = ano - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Existem {} pessoas maior de idade e {} pessoas menor de idade!'.format(maior, menor))


"""Crie um programa que leia o ano de nascimento 
de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas
já são maiores"""