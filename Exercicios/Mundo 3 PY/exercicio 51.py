linha1 = []
linha2 = []
linha3 = []
conteudo = []
for l in range(0, 3):
    conteudo.append(int(input('Digite um numero: ')))
    linha1.append(conteudo[:])
    conteudo.clear()
for l in range(0, 3):
    conteudo.append(int(input('Digite um numero: ')))
    linha2.append(conteudo[:])
    conteudo.clear()
for l in range(0, 3):
    conteudo.append(int(input('Digite um numero: ')))
    linha3.append(conteudo[:])
    conteudo.clear()
print(linha1)
print(linha2)
print(linha3)



"""Crie um programa que crie uma matriz de dimenssão 3x3 e preencha com valores lidos pelo teclado:
No final, mostre a matriz na tela, com a formatação correta.
"""