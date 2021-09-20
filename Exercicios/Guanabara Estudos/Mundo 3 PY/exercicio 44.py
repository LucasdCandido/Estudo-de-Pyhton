valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = input('Gostaria de digitar mais um numero? [S/N] ').upper().strip()[0]
    if resposta in 'N':
        break
print(sorted(valores))

"""Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
Caso o numero já exista la dentro, ele não sera adicionado.
No final, serão exibidos todos os valores unicos digitados em ordem crescente.
"""