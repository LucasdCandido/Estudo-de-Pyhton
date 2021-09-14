vetor = []
soma = 0
for c in range(0,10):
    vetor.append(int(input('Numero: ')))
for c in vetor:
    soma += c**2
    print(soma)