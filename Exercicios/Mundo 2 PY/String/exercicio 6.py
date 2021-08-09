nome = str(input('Digite seu nome: ')).upper().strip()
n =""
for i in range(len(nome)):
    n += nome[i]
    print(n)
for i in range(len(nome)):
    print(nome)
    nome=nome[:-1]
    