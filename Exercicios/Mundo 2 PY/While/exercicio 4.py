cidA = int(input('População do pais A: '))
while cidA <0:
    cidA = int(input('População do pais A: '))
taxaA=float(input('Taxa de crescimento da populção: '))
cidB = int(input('População do pais B: '))
while cidB < 0:
    cidB = int(input('População do pais B: '))
taxaB=float(input('Taxa de crescimento da cidade B: '))
tA = taxaA /100
tB = taxaB /100
ano = 0
while cidA <= cidB:
    cidA = cidA * tA
    cidB = cidB * tB
    ano = +1




"""Supondo que a população de um pais A seja da ordem de 80000 habitantes com uma taxa anual
de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento
de 1.5%. Faça um programa que calcule e escreva o numero de anos necessarios para que a população do pais A
ultrapasse ou iguale a população do pais B, mantidas as taxas de crescimento
"""