from datetime import date
num = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual-num
falta = 18-idade
passou = idade-18
if idade < 18:
    print('Deve se alistar daqui {} anos'.format(falta))
elif idade == 18:
    print('Você deve se apresentar a uma junta militar para se alistar no exercito!')
else:
    print('Ja passou o tempo de alistamento por {} anos'.format(passou))



"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar
-Se é a hora de se alistar
-Se já passou do tempo do alistamento
Seu prograna também devera mostrar o tempo que falta ou que passou do prazo"""