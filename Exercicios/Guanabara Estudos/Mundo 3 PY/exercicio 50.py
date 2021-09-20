valores = []
par = []
impar = []
for c in range(0, 7):
    valores.append(int(input('Digite um numero: ')))
for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
par.sort()
impar.sort()
print(par)
print(impar)



"""Crie um programa onde o usuario possa digitar sete valores numeros e cadastre-os em uma lista unica
que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em odem crescente.
"""