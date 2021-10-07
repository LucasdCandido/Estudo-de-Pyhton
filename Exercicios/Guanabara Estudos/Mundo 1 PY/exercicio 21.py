nome = str(input('Digite seu nome completo: ')).strip()
nom = nome.lower()
print('A letra A no seu nome aparece {} vezes.'.format(nom.count('a')))
print('A primeira letra A no seu nome aparace na posição {}.'.format(nom.find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(nom.rfind('a')+1))

"""Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra A
Em que posição ela aparece a primeira vez
Em que posição ela aparece a ultima vez"""