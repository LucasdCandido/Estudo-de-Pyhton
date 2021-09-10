notas = []
for c in range(0,4):
    notas.append(float(input('Digite uma nota: ')))
media = sum(notas)/len(notas)
print(notas, media)