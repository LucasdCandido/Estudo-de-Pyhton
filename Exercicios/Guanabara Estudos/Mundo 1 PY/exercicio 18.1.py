def unidades(numero):
    if numero < 10:
        u = numero // 1 % 10
        print(f'O numero que você digitou foi:\nUnidade: {u}')
    elif numero < 100:
        u = numero // 1 % 10
        d = numero // 10 % 10
        print(f'O numero que você digitou foi:\nDezena:  {d}\nUnidade: {u}')
    elif numero < 1000:
        u = numero // 1 % 10
        d = numero // 10 % 10
        c = numero // 100 % 10
        print(f'O numero que você digitou foi:\nCentena: {c}\nDezena:  {d}\nUnidade: {u}')
    elif numero < 10000:
        u = numero // 1 % 10
        d = numero // 10 % 10
        c = numero // 100 % 10
        m = numero // 1000 % 10
        print(f'O numero que você digitou foi:\nMilhar:  {m}\nCentena: {c}\nDezena:  {d}\nUnidade: {u}')


numero = int(input('Digite um numero de 0 a 9999: '))
unidades(numero)