tab = int(input('Qual numero gostaria de saber a Tabuada: '))
print('A Taboada do {} fica assim: '.format(tab))
cont = 0
for c in range(1, 11):
    cont = cont +1
    t = tab*cont
    print('{} x {} = {}'.format(tab, cont, t))
    



"""Refaça o desafio 9, mostrando a tabuada de 
um numero que o usuario escolher, só que agora
ultilizando um laço for"""