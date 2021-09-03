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
exceliquido = exce-506.1
print('Valor excedente menos o VT R$ {:.2f}'.format(exceliquido))