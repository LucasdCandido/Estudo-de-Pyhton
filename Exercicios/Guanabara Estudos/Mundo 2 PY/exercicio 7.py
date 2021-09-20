from time import sleep
print("""Ola, seja bem vindo!
      Vamos juntos aqui, criar um triangulo, dentro da classificação de 
      três tipos diferentes, Equilatero, Isoceles e Escaleno.
      E pra isso temos que atender ao coeficiente do triangulo que é, uma reta não pode ser maior que 
      a soma das outras duas retas e isso se aplica a todas as retas do triangulo.
      Bom, agora que você já esta munido das informações, vamos ao triangulo:""")
sleep(1.5)
r1 = int(input('Digite o tamanho da reta: '))
r2 = int(input('Digite o tamanho da outra reta:'))
r3 = int(input('Digite o tamanho da ultima reta:'))
sleep(1)
if r1<(r2+r3) and r2<(r3+r1) and r3<(r1+r2):
    if r1==r2 and r2==r3 and r3==r1:
        print('Esse é um triangulo Equilatero!')
    elif r1!=r2 and r2!=r3 and r1!=r3:
        print('Esse é um triangulo Escaleno!')
    elif r1<(r2==r3) or r2<(r3==r1) or r3<(r1==r2) or r1>(r2==r3) or r2>(r3==r1) or r3>(r1==r2):
        print('Esse triangulo é um Isoceles!') 
else:
    print('Você não esta lembrando de usar o coeficiente do triangulo para decidir suas retas!')
"""Refaça o Desafio 035 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado:
-Equilatero:todos os lados iguais
-Isosceles:dois lados iguais
-Escaleno:todos os lados diferentes"""