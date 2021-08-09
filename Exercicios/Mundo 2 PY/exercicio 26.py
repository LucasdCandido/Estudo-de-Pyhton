primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
cont2 = 1
n = 1
while n !=0:
    while cont < 10:
        print('{} -->'.format(termo), end="")
        termo = primeiro + razao
        cont += 1
        cont2 += 1
    print('PAUSA')
    n = int(input('Quantos termos a mais você gostaria de ver? '))
    cont = 10 - n
print('Foram mostrado {} termos da PA.'.format(cont2))



'''Refaça o desafio 51, lendo o primeiro termo e a razão da PA, mostrando os 10 primeiros 
termos da progração usando a estrutura while'''