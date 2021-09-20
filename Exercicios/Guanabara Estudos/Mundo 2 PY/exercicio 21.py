somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0
for c in range(1, 5):
    print('~~~~~~~~~~~~{}ª PESSOA! ~~~~~~~~~~~~~~~~'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1
mediaidade = somaidade / 4
print('A media de idade é de {} anos: '.format(mediaidade))
print('O homem mais velho é {} com a idade de {} anos!'.format(nomevelho, maioridadehomem))
print('A quantidade de mulheres com menos de 20 anos é {}!'.format(mulher))



"""Desenvolva um programa que leia o nome, idade e
sexo de 4 pessoas. No final do programa mostre:
A media de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres tem menos de 20 anos."""