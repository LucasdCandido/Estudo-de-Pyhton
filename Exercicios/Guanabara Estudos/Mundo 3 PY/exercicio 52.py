matriz =[[0,0,0],[0,0,0],[0,0,0]]
somapar = maior = coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end="")
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
for l in range(0, 3):
    coluna += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(somapar)
print(coluna)
print(maior)


"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores na terceira coluna.
C) O maior valor da segunda linha.
"""