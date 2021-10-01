from random import sample
import random

def lista_apresentação(lista):
    print(f'A lista de alunos que vai aprensentar é: {sample(lista, k = len(lista))}')


lista = []
for c in range(5):
    lista.append(input('Digite os nomes dos alunos: '))

lista_apresentação(lista)