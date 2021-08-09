"""nome = str(input('Digite seu nome: ')).upper().strip()
while len(nome)>0:
    print(nome)
    nome = nome[:-1]"""

nome = str(input('Digite seu nome: ')).upper().strip()
for i in range(len(nome)):
    print(nome)
    nome = nome[:-1]