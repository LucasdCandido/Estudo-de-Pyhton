notas = []
contador = 0
for c in range(0,10):
    nome = input('Digite o nome do aluno: ')
    for c in range(0,4):
        notas.append(float(input(f'Digite a {c+1} nota: ')))
    media = sum(notas)/len(notas)
    notas.clear()
    if media >= 7:
        contador += 1
    print(media)
print(f'Dos 10 alunos, {contador} tiraram media de  notas de 7 ou mais')