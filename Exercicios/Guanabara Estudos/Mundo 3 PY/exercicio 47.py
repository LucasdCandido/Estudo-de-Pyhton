valores = []
par = []
impar = []
reposta = ""
contadorpar = contadorimpar = 0
while True:
    valores.append(int(input('Digite um numero: ')))
    resposta = input('Gostaria de continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
for v in valores:
    if v % 2 == 0:
        par.append(v)
        contadorpar += 1
    else:
        impar.append(v)
        contadorimpar += 1
print(f'A lista de numeros pares é {par}\nA lista de numeros impares é {impar}\nForam digitados {contadorpar} numeros pares\nForam digitados {contadorimpar} numeros impares')




"""Crie um programa que valide varios numeros e colocar em uma lista.
Depois disso, crie duas listas extras que vão contarapenas o numeros pares e 
os valores impares digitados, respectivamente.
Ao final, mostre o conteudo das tres listas geradas.
"""