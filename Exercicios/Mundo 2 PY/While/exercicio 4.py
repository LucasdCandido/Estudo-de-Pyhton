cidA = float(input('Digite o valor da população da cidade A: '))
while cidA < 0:
    cidA = float(input('Digite um valor valido da população da cidade A: '))
taxa_A = float(input('Digite o valor da taxa de crescimento da cidade A: '))
while taxa_A < 0:
    taxa_A = float(input('Digite uma taxa de crescimento valida: '))
cidB = float(input('Digite a população da cidade B: '))
while cidB < 0:
    cidB = float(input('Digite um valor valido da popupação da cidade B: '))
taxa_B = float(input('Digite o valor da taxa de crescimento da cidade B: '))
while taxa_B < 0:
    taxa_B = float(input('Digite uma taxa de crescimento valida: '))
ano = 0
while cidA < cidB:
    ano += 1
    cidA = float((1 + (taxa_A/100))* cidA)
    cidB = float((1 + (taxa_B/100))* cidB)
    print('{:.2f}'.format(cidA))
    print('{:.2f}'.format(cidB))
print('Após {} anos, a cidade A ultrapassou a população da cidade B.'.format(ano))




"""Supondo que a população de um pais A seja da ordem de 80000 habitantes com uma taxa anual
de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento
de 1.5%. Faça um programa que calcule e escreva o numero de anos necessarios para que a população do pais A
ultrapasse ou iguale a população do pais B, mantidas as taxas de crescimento
"""