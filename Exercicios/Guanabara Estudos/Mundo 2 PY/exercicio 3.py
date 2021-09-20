from time import sleep
print("""Vamos então fazer a comparação de alguns numeros inteiros.
      Vamos comparar para ver qual numero inteiro é maior, menor ou se em algum dos casos os numero inteiro 
      são os mesmo!""")
sleep(0.5)
n1 = int(input('Digite aqui o numero inteiro para comparação: '))
sleep(0.5)
n2 = int(input('Digite aqui o outro numero inteiro: '))
sleep(0.5)
if n1 == n2:
    print('Não existe numero maior ou menos, os dois são iguais!')
elif n1>n2:
    print('O primeiro numero o {} é o maior!'.format(n1))
else:
    print('O segundo numero o {} é o maior!'.format(n2))



"""Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais"""