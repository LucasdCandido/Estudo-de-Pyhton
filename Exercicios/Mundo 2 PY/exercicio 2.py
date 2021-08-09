from time import sleep
print("""Vamos fazer algumas alterações de base numerica!
      Hoje vamos fazer alterações de base de Decimal para:
      Binario, Octal e Hexadecimal!""")
sleep(1.5)
base = str(input('Você gostaria transformar seu Decimal para qual base? ')).lower().strip()
sleep(1)
num = int(input('Qual seu numero Decimal para ser convertido: '))
sleep(1)
bin = format(num, 'b')
oct = format(num, 'o')
hex = hex(num).strip('0x')
if base == "binario":
    print('Seu numero em Binario fica: {}'.format(bin))
elif base == "octal":
    print('Seu numero em Octal fica: {}'.format(oct))
elif base == "hexadecimal":
    print('Seu numero em Hexadecimal fica: {}'.format(hex))



"""Escreva um programa que leia um numero inteiro qualquer e que peça para o usuario escolher qual sera a 
base de conversão:
-1 para binario
-2 para octal
-3 para hexadecimal"""