palavras = ('cadarco', 'remedio', 'tijolo', 'ralapenho', 'estrutura')
for palavra in palavras:
    print(f'\n{palavra:<15}', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
        



"""Crie um programa que tenha uma tupla com varias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""