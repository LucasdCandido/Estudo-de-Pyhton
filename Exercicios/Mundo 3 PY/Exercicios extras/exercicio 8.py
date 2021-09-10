pessoa = []
nome = []
cadastro = []
altura = []
idade = []
for c in range(0,2):
    nome.append(input('Nome: ').upper().strip())
    altura.append(float(input('Altura: ')))
    idade.append(int(input('Idade: ')))
    pessoa.append(nome[:])
    pessoa.append(altura[:])
    pessoa.append(idade[:])
    cadastro.append(pessoa[:])
    pessoa.clear()
print(cadastro)