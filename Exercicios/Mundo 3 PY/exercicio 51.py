matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um numero [{l}, {c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end="")
    print()



"""Crie um programa que crie uma matriz de dimenssão 3x3 e preencha com valores lidos pelo teclado:
No final, mostre a matriz na tela, com a formatação correta.
"""