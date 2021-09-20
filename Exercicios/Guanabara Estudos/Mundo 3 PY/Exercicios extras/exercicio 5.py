numeros = []
par = []
impar = []
for c in range(0,20):
    numeros.append(int(input('Digite um numero: ')))
for c in numeros:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'{numeros} {par} {impar}')