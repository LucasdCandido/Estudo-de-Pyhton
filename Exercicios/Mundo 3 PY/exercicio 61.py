'''
def area(largura, comprimento):
    total = largura*comprimento
    print(f'A area total é de {total}')



area(
    largura=float(input('Digite a largura da area: ')),
    comprimento=float(input('Digite o comprimento da area: '))
)
'''
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area de um terreno {largura} x {comprimento} é de {a}m².')
    
    
    
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)



"""
Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a area do terreno.
"""