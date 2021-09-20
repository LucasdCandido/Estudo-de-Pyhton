import random
a1 = input('Nome do aluno: ')
a2 = input('Nome do aluno: ')
a3 = input('Nome do aluno: ')
a4 = input('Nome do aluno: ')
a5 = input('Nome do aluno: ')
a6 = input('Nome do aluno: ')
a7 = input('Nome do aluno: ')
a8 = input('Nome do aluno: ')
a9 = input('Nome do aluno: ')
a10 = input('Nome do aluno: ')

list = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]

sort = random.choice(list)
print ('O aluno que ira apagar a lousa é: {}'.format (sort))



#Um professor quer sortear um dos alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.