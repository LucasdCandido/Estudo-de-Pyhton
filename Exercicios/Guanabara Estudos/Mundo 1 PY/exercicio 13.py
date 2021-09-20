from math import cos, sin, tan, radians

x = float (input('Digite o angulo para ser feito o calculo de seno, cosseno e tangente: '))
rad = radians(x)
cos = cos(rad) 
sin = sin(rad) 
tan = tan(rad) 

print ('O cosseno, seno e tangente do mesmo são: {:.3f}, {:.3f}, {:.3f}'.format(cos, sin, tan))



#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.