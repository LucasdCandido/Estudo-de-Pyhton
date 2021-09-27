#def é uma palavra reservada para a construção de uma função
#a palavra após def vem como o nome da frunção e seus parametros dentro do parenteses
def antesdepois(n):
    #dentro da função vem ou o programa que você vai usar ou um print para realização a função do programa
    mais = n+1
    menos = n-1
    print(f'O numero {n} tem com valor anterior {menos} e o numero seguinte {mais}')

#depois dentro do seu programa que traz as funcionalidades que vão ser usadas dentro da função fazendo com que você possa ultilizar essa função muito mais rapido e pratico em varias partes do seu programa
n = int(input('Digite um numero: '))
antesdepois(n)