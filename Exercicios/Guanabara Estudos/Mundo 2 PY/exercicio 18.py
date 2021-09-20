

frase = str(input('Digite uma frase: ')).strip().lower()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')


"""Crie um programa que leia uma frase qualquer e 
diga se ela é um palidromo, desconsiderando os 
espaços
EX APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
ANOTARAM A DATA DA MARATONA"""