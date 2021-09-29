'''
multiple-inheritance - 2
Python suporta multiplas heranças
Ultiliza a ordem de primeira profundidade quando esta procurando por um metodo.
Esse padrão de procura é chamado MRO (Method Resolution Order)
Esse é o segundo exemplo, que mostra a pesquisa de 'dothis()'.
Tanto A quanto C contem 'dothis()'. Vamos traçar como a pesquisa acontece.
Contanto que a saide de MRO usando a pesquisa de primeira profundidade, vai começar com a classe D, depois B, A e por final C.
Vamos procurar por 'dothis()' que foi definido na classe 'C'.
A pesquisa passa por D->B->A->C.
Desde que a classe 'A' não tem o 'dothis()', a pesquisa vai retornar a classe C e encontrar la.
'''

class A(object):
    def dothat(self):
        print('Doing this in A')


class B(A):
    pass


class C(object):
    def dothis(self):
        print('\n Doing this in C')


class D(B, C):
    '''
    Multiplas heranças, D herda tanto de B quanto de C
    '''
    pass

d_intance = D()

d_intance.dothis()

print('\n Print the Method Resolution Order')
print(D.mro())