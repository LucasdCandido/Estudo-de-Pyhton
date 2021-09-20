sal = float(input('Entre com o seu salario: R$'))
if sal<1250.00:
    sc = (sal*.15)+sal
else:
    sc = (sal*.1)+sal
    
print('Seu salario de R${:.2f} agora vai ser R${:.2f}'.format(sal, sc))



"""Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""