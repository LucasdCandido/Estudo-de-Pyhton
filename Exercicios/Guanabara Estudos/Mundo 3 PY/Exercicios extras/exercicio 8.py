altura = []
idade = []
nome = []
pessoa = []
for c in range(0,2):
    nome.append(input('Nome: ').strip())
    idade.append(int(input('Idade: ')))
    altura.append(float(input('Altura: ')))
    pessoa.append([nome[:],idade[:],altura[:]])
    nome.clear()
    idade.clear()
    altura.clear()
pessoa.reverse()
for c in pessoa:
    print(f'{c} ',end="")
    