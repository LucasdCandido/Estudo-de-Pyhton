n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
opcao = 0
while opcao != 5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa """)
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            print('Primeiro valor é maior!')
        elif n1 == n2:
            print('Os valores são iguais! ')
        else:
            print('Segundo valor é maior!')
    elif opcao == 4:
        print('Digite os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print("Opção invalida. Tente novamente! ")
    print('=-='*10)
print('Fim do programa')



'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa'''