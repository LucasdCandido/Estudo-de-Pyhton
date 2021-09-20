vetor1 = []
vetor2 = []
vetor3 = []
vetores = []
for c in range(0,10):
    vetor1.append(int(input('Digite um numero: ')))
    vetor2.append(int(input('Digite um numero: ')))
    vetor3.append(int(input('Digite um numero: ')))
    vetores.append(vetor1[:])
    vetores.append(vetor2[:])
    vetores.append(vetor3[:])
    vetor1.clear()
    vetor2.clear()
    vetor3.clear()
print(vetores)