def conversordemoeda(real):
    dolar = real*5.35
    print(f'O valor de R$ {real} em dolar fica $ {dolar:.2f}')

real = float(input('Digite qual o valor de real para ser convertido em dolar: R$ '))
conversordemoeda(real)