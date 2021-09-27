def tabuada(n):
    #mesmo dentro da função que criamos podemos ultilizar o o laço for, e fazer calculos dentro do print para apresentar resuldados
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')

n = int(input('Digite um valor para ver a tabuada: '))
tabuada(n)