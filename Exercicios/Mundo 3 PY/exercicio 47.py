variavel = []
par = []
impar = []
resposta = ""
contador = 0
while True:
    variavel.append(int(input('Digite um numero: ')))
    contador += 1
    resposta = input('Gostaria de digitar mais numeros? ').upper().strip()[0]
    if resposta == 'N':
        break
for v in variavel:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(variavel, par, impar)




"""Crie um programa que valide varios numeros e colocar em uma lista.
Depois disso, crie duas listas extras que vão contarapenas o numeros pares e 
os valores impares digitados, respectivamente.
Ao final, mostre o conteudo das tres listas geradas.
"""