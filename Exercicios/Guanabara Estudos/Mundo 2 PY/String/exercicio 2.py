nome = str(input('Digite seu nome para ser escrito ao contrario: ')).strip().upper()
inver = ' '
for letra in range(len(nome) -1, -1, -1):
    inver += nome[letra]
print('Seu nome invertido fica {}'.format(inver))