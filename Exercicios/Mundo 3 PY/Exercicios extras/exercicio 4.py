letras = []
contador = 0
for c in range(0,10):
    letras.append(input('Digite uma letra: ').upper().strip()[0])
for c in letras:
    if c in 'AEIOU':
        contador += 1
        print(f'{c} ', end="")
print(contador)