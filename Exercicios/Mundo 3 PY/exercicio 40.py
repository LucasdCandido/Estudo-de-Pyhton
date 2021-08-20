numero1 = numero2 = numero3 = numero4 = numeros = m = contador9 = contadorpar = par = 0
numero1 = int(input('Digite um numero: '))
while numero1 < 0:
    numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
while numero2 < 0:
    numero2 = int(input('Digite outro numero: '))
numero3 = int(input('Digite outro numero: '))
while numero3 < 0:
    numero3 = int(input('Digite outro numero: '))
numero4 = int(input('digite outro numero: '))
while numero4 < 0:
    numero4 = int(input('Digite outro numero: '))
numeros = (numero1, numero2, numero3, numero4)
for c in range(0, len(numeros), 1):
    m = numeros[c]
    if m == 9:
        contador9 += 1
    par = m % 2
    if par == 0:
        contadorpar += 1
print(f'O numero 9 foi encontrado {contador9} vezes.')
print(f'O numero 3 aparece na localização {numeros.index(3)} da string')
print(f'A quantidade de numeros pares que aparece é {contadorpar}')


"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os numeros pares.
"""