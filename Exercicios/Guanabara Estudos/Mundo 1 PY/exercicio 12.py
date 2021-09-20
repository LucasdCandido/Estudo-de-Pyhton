import math
x = float (input ('Digite o valor do cateto oposto: '))
y = float (input ('Digite o valor do ceteto adjacente: '))
hipot = math.hypot(x,y)
print ('Sendo o cateto oposto {} e o cateto adjacente {} o valor da hipotenusa é {:.2f}' .format (x, y, hipot))


#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo mostrar o comprimento da hipotenusa