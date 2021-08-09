vp = float (input ('Qual o valor do produto: R$'))
vd = vp*0.05
vf = vp-vd

print ('O produto no valor de R${:.2f}, com o desconto de R${:.2f} fica no valor de R${:.2f}' .format (vp,vd,vf))



#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.