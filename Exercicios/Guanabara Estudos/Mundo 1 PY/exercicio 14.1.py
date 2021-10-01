from random import choice

def nome_escolhido(lista):
    print(f'O nome escolhido foi: {choice(lista)}')


lista = []
for c in range(10):
    lista.append(input('Digite o nome de um aluno para ser selecionado: '))

nome_escolhido(lista)