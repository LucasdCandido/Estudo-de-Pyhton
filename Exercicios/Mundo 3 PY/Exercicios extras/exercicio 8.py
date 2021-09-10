pessoa = []
nome = []
altura = []
idade = []
for c in range(0,2):
    nome.append(input('Nome: ').upper().strip())
    altura.append(float(input('Altura: ')))
    idade.append(int(input('Idade: ')))
    pessoa.append([nome[:], altura[:], idade[:]])
    nome.clear()
    altura.clear()
    idade.clear()
print(pessoa)