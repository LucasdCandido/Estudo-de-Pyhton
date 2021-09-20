valores = []
contador = 0
resposta = ""
while True:
    valores.append(int(input('Digite um numero: ')))
    contador += 1
    resposta = input('Gostaria de digitar mais um numero? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
print(contador)
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('Foi digitado o numero 5 nessa lista!')
else:
    print('Não foi digitado o numero 5 nessa lista!')



"""Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, mostre:
A) Quantos numeros foram digitados.
B) A lista de valores ordenados de forma decrescente.
C) Se o valor 5 foi digitado e esta ou não na lista.
"""