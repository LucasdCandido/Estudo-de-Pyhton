
nome = str(input('Olá, qual o seu nome: '))
prod = float(input('Qual o valor do produto: '))
print('{}, vamos avaliar os descontos possiveis o seu produto!'.format(nome))
forma = str(input('Prefere pagamento A vista, Cheque, A vista no credito ou Parcelado: ')).lower().strip()
if forma == 'parcelado':
    parcel = int(input('Digite quantas parcelas você prefere: '))
    parc = (prod*.2)+prod
    parce = parc/ parcel
    parc = (prod*.2)+prod
    parce = parc/ parcel
    par = prod/2
elif forma == 'a vista':
    forma = 'a vista'
elif forma == 'cheque':
    forma = 'cheque'
elif forma == 'a vista no credito':
    forma ='a vista no credito'
else:
    print('Vamos ver quanto vai ficar!')
avd = prod*0.1
avc = prod*0.05
if forma == 'a vista':
    print('Pagando a vista fica R${:.2f}'.format(avd))
elif forma == 'cheque':
    print('Pagando com o cheque fica R${:.2f}'.format(avd))
elif forma == 'a vista no credito':
    print('Pagando a visto no credito fica R${:.2f}'.format(avc))
elif parcel == 2:
    print('Seu produto vai ficar R${:.2f} o valor de cada parcela fica R${:.2f}'.format(prod, par))
else:
    print('Seu produto vai ficar R${:.2f} o valor de cada parcela fica R${:.2f}'.format(parc, parce))


"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:
-A vista dinheiro/cheque: 10% de desconto
-a vista no cartão:5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros"""