from time import sleep
nome = str(input('Digite seu nome: '))
print("""Olá, {}!
      Vamos agora descobrir se você foi aprovado ou não:
      Vocâ vai colocar suas notas semestrais e ver se você tem uma media suficiente 
      para ser aprovado, reprovado ou se vai ficar de recuperação!
      Boa sorte!""".format(nome))
sleep(1)
med = float(input('{} Digite aqui sua nota: '.format(nome)))
med2 = float(input('{} Digite aqui sua outra nota: '.format(nome)))
m = (med+med2)/2
sleep(1)
print('Sua media foi {}.'.format(m))
sleep(1)
if m<5:
    print('Você foi REPROVADO!')
elif m<6.9:
    print('Você esta de RECUPERAÇÃO!')
else:
    print('Parabéns, você foi APROVADO!')



"""Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a media atingida:
-Media abaixo de 5.0: Reprovado
-Media entre 5.0 e 6.9: Recuperação
-Media 7.0 ou superior: Aprovado"""