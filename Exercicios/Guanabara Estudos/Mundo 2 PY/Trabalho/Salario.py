salario = float(input('Digite seu salario: '))
vt = salario*0.06
inss = salario*0.075
liquido = salario-vt-inss
print('''O valor do salario liquido é de R$ {:.2f},
      o valor descontado de VT do salario é de R$ {:.2f} e o valor do inss é de R$ {:.2f}'''.format(liquido, vt, inss))
pag = float(input('Digite quanto foi pago: R$ '))
print('Valor depositado completo neste mês R$ {:.2f}'.format(pag))
exce = pag - liquido
print('O valor excedente do salario liquido é de R$ {:.2f}'.format(exce))
dia = int(input('Digite quantos dias de trabalho no mês: '))
bu = float(input('Digite o valor da passagem do Bilhete Unico: '))
bom = float(input('Digite o valor da passagem do Bilhete Bom: '))
inte = float(input('Digite o valor da integração do Bilhete unico entre onibus e trem: '))
valor_bu = (dia*(bu*2))+(dia*(inte*2))
valor_bom = (dia*(bom*2))
restante = pag - valor_bom - valor_bu
print(f'O valor do VT ficou {valor_bu+valor_bom:.2f}, o valor no BU é {valor_bu:.2f} e o valor do BOM é {valor_bom:.2f},o salario é {restante:.2f}.')