numeros = []
for c in range(0,10):
    numeros.append(int(input('Digite um numero: ')))
numeros.sort(reverse=True)
for c in numeros:
    print(f'{c} ',end="")