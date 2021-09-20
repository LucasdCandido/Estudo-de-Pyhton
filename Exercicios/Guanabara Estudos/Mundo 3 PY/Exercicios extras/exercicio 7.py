numeros = []
multiplos = []
for c in range(0,5):
    numeros.append(int(input('Digite um numero: ')))
for c in numeros:
    multiplos.append(c*2)
for c in numeros:
    print(f'{c} ', end="")
print()
print(f'{sum(numeros)} ',end="")
print()
for c in multiplos:
    print(f'{c} ',end="")