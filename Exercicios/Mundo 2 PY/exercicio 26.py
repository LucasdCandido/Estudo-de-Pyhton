termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao do termo da PA: '))
t = termo
c = 1
n = 1
while c != 0:
    while c <= 10:
        print('{} --> '.format(t), end="")
        t += termo + razao
        c += 1
        n += 1
    print('PAUSA')
    c = int(input('Quantos termos a mais gostaria de ver? '))
print('Foram apresentados {} termos da PA'.format(n))




'''Refaça o desafio 51, lendo o primeiro termo e a razão da PA, mostrando os 10 primeiros 
termos da progração usando a estrutura while'''