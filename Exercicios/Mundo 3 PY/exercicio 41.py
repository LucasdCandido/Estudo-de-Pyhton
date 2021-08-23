produtos = ('Sabão em Pó', 27.99, 'Leite', 4.87, 'Picanha', 37.99, 'Papel Aluminio', 3.99, 'Mouse', 17.99)
"""a1, a2, b1, b2, c1, c2, d1, d2, e1, e2 = produtos
print('=-='*30)
titulo = 'LISTA DE COMPRA'
print(titulo.center(80))
print('=-='*30)
print(f'''
                        {a1} ------------- R$ {a2}
                        {b1} ------------------- R$ {b2}
                        {c1} ----------------- R$ {c2}
                        {d1} ---------- R$ {d2}
                        {e1} ------------------- R$ {e2}''')"""
for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:-<30} R$ ', end='')
    else:
        print(f'{produtos[posicao]:>6}')



"""Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia.
No final, mostre um listagem de preços, organizando os dados em forma tabular.
"""