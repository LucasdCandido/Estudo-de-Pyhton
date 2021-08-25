valores = []
novos = []
contador = maior = menor = maiormenor = maiormenor2 = maiormenor3 = 0
for c in range(0,5):
    valores.append(int(input('Digite um numero: ')))
for v in valores:
    contador += 1
    if contador == 1:
        maior = menor = menormenor = maiormenor2 = v
        novos.append(v)
    else:
        if menor >= v:
            menor = v
            novos.lappend(menor)
        if maior <= v:
            maior = v
            novos.append(maior)
        if maiormenor > menor:
            menormaior = v
            novos.insert((novos.index(menor)), menormaior)
        if maiormenor2 > maiormenor:
            maiormenor2 = v
            novos.insert((novos.index(maiormenor)), maiormenor2)
        if maiormenor3 > maiormenor2:
            maiormenor3 = v
            novos.insert((novos.index(maiormenor2)), maiormenor3)
print(novos)



"""Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista,
já na posição correta de inserção(sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""