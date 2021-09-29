'''
multiple-inheritance - 3
Pyhton suporta multiplas heranças e usa o metodo de procura de primeira profundidade.
Esse padrão de procura é chamado MRO (Method Resolution Order).
Exemplo para herança 'Diamond Shape'.
Pesquisar pode ficar complicada com multiplas heranças de classe para multiplas heranças de classes parentes.
Em ordem de evitar ambiguidade enquanto procura o metodo em varias classes, para o Python 2.3, o MRO vai procurar recursos adicionais.
Ainda faz uma pesquisa de primeira profundidade, porem se ocorre em uma classe multiplas vezes no caminho MRO, ele remove as primeiras ocorrencias e continua depois.
No exemplo abaixo, classe 'D' herda de 'B' e 'C'.
E tanto 'B' quanto 'C' herdam de 'A'.
Ambos 'A' e 'C' tem o metodo 'dothis()'.
Nos intanciamos 'D' e chamamos o metodo 'dothis()'.
Por definição, a procura deve seguir D->B->A->C->A.
Porem em Python 2.3, em ordem de reduzir o tempo de pesquisa, o MRO pula as classes que ocorrem multiplas vezes no caminho.
Portanto a pesquisa vai ser D->B->C->A.
'''

class A(object):
    def dothis(self):
        print('doing this in A')

    
class B(A):
    pass


class C(A):
    def dothis(self):
        print('doing this in C')


class D(B, C):
    pass


d_instance = D()
d_instance.dothis()

print('\n Print the Method Resolution Order')
print(D.mro())