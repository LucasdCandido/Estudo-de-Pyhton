nc = input ('Escreva seu nome completo: ')

print ('Seu nome com letras maiusculas é {} \nSeu nome com letras minuscula é {} \nSeu nome ao todo contem {} letras \nSeu primeiro nome tem {} letras.'.format((nc.upper()),(nc.lower()),(len(nc.translate({ord(' '):None}))),(len(nc.split()[0]))))
"""nc = nc.upper()
print (nc)
nc = nc.lower()
print (nc)

print (len(nc.translate({ord(' '): None})))

print (len(nc.split()[0]))"""
       


"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas
O nome com todas minusculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome"""