ano = int(input('Digite o ano para saber se é um ano bissesto: '))


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bissesto.'.format(ano))
else:
    print('O ano {} não é um ano bissesto.'.format(ano))



"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""