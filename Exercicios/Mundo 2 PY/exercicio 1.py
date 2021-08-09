from time import sleep
nome = str(input('Olá, qual o seu nome? '))
print("""Bem vindo(a) {}! Vamos fazer o calculo para ver se é possivel fazer a aprovação do seu
      financiamento.
      Vamos precisar de algumas informações para poder fazer a possibilidade do financiamento!""".format(nome))
sleep(0.5)
sala = float(input('Qual o valor do seu salario mensal: '))
casa = float(input('Qual o valor da casa que você quer financiar: '))
parc = float(input('Em quantas parcelas pretendo fazer o financiamento: '))

vp = casa/parc
ps = sala*0.30
sleep(1)
if vp<ps:
    print('Parabéns! Seu financiamento foi aprovado. As parcelas vão ficar no valor de R${:.2f}'.format(vp))
else:
    print("""Desculpa, infelizmente o financiamento leva em consideração que a parcela não pode ser maior que 30% do seu
          salario e nesse caso o parcelamento ficou em R$ {:.2f} e 30% do seu salario é R$ {:.2f}""".format(vp, ps))

"""Escreva um programa que vai aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
calcule o valor da prestação mensal, sabendo que ela não pode exceder 
30% do salario ou então o emprestimo sera negado."""