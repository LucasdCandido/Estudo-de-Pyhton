'''from random import uniform
from random import randint
alunos = []
altura = []
idade = []
media = 0
for c in range(0,10):
    altura.append(uniform(120.5, 199.5))
    idade.append(randint(10, 25))
    alunos.append([idade[:], altura[:]])
    altura.clear()
    idade.clear()
contador = 0
for l in range(len(alunos)):
    if alunos[l] <= 13:
        print(alunos[l])'''
idades = [10, 15, 9, 22, 13, 12, 14]
alturas = [1.60, 1.35, 1.76, 1.98, 1.77, 1.66, 1.80]

mediaAltura = sum(alturas)/len(alturas)

quantidadeAlunos = 0
for i in range(0, len(idades)):
    if idades[i] > 13 and alturas[i] < mediaAltura:
        quantidadeAlunos = quantidadeAlunos + 1

print (str(quantidadeAlunos) + " alunos possuem mais de 13 anos e altura inferior a  media de altura dos alunos")