def media(m):
    #aqui foi ultilizado sum() e len(), que servem para fazer a soma total e a contagem total de itens dentro ou de uma lista ou de uma string respectivamente
    media = sum(m)/len(m)
    print(f'A primeira nota do aluno {m[0]} e a segunda nota do aluno {m[1]} tem como media {media}')
#aqui foi iniciado uma lista para fazer o armazenamento de mais  de um numero
m = []
#aqui foi ultilizado um laço for, já temos a quantidade que vão limitar o laço, usar o for é mais eficiente, conseguindo obter o resultado esperado
for i in range(0,2):
    m.append(float(input('Digite a nota do aluno: ')))

media(m)