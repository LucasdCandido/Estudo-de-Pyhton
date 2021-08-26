valores = []
for c in range(0, 5):
    v = int(input('Digite um numero: '))
    if c == 0 or v > valores[-1]:
        valores.append(v)
    else:
        posicao = 0
        while posicao < len(valores):
            if v <= valores[posicao]:
                valores.insert(posicao, v)
                break
            posicao += 1
print(valores)



"""Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista,
já na posição correta de inserção(sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""