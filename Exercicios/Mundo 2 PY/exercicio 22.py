sexo = str(input('Digite seu sexo [M/F]: ')).upper()[0].strip()

while sexo not in 'FfMm':
    sexo = str(input('Sexo invalido! Por Favor, digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'Ff':
        sexo = 'Feminino'
    elif sexo in 'Mm':
        sexo = 'Masculino'
print('Seu sexo é {}!'.format(sexo))



'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os
valores 'M' ou 'F' caso esteja errado, peça a digitação novamente até
ter um valor correto.'''