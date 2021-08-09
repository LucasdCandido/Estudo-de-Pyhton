import random

n1 = input ('Digite o nome do aluno: ')
n2 = input ('Digite o nome do aluno: ')
n3 = input ('Digite o nome do aluno: ')
n4 = input ('Digite o nome do aluno: ')

list = [n1, n2, n3, n4]

nomes = random.sample(list, k=4)

print ('A lista dos sorteados é: {}.' .format(nomes))





#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos a mostrar a ordem sorteada.