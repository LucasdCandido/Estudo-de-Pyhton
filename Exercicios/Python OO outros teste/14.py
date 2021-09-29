'''
multiple-inheritance - 1
Python suporta multiplas heranças e usa primeira orden de profundidade quando procura por um metodo.
Isso vai procurar o padrão chamado MRO (Method Resolution Order)
Esse é o primeiro exemplo, que mostra a pesquisa por funções comuns com mesmo nome 'dothis()', o que vamos continuar em outros exemplos.
Conforma a saida de MRO, começa na classe D, depois B, A e por fim, C.
Tanto A quanto C contem 'dothis()'. Vamos traçar como a pesquisa acontece.
Conforme a saida de MRO, começa na classe D, depois B, A e por fim C.
classe 'A' define 'dothis()' e a pesquisa termina ali. Não vai até C.
O MRO vai mostrar a resolução total do caminho mesmo se não for percorrido.
O metodo de pesquisa segue o fluxo neste caso assim: D->B->A->c
'''

class A(object):
    def dothis(self):
        print('Doing this in A')

    
class B(A):
    pass


class C(object):
    def dothis(self):
        print('Doing this in C')

    
class D(B, C):
    pass


d_instance = D()
d_instance.dothis()
'''
Isto deve imprimir da classe A.
'''

print('\n Print the Method Resolution Order')
print(D.mro())