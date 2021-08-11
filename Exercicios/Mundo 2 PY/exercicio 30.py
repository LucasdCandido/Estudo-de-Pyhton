soma = cont = media = numero = maior = menor = 0
f = 'S'
while f in 'S':
    numero = int(input('Digite um numero inteiro para tirar a media: '))
    soma = soma + numero
    cont += 1
    f = str(input('Você gostaria de digitar mais um numero? [N/S] ')).upper().strip()[0]
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma / cont
print('Foram digitados {} numeros e a media entre eles é de {}'.format(cont, media))
print('O maior numero apresentado é {} e o menor numero é {}'.format(maior, menor))

'''Crie um programa que leia varios numeros inteiros pelo teclado.
No final da execução, mostre a media entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar
ao usuario se ele quer ou não continuar a digitar valores'''