'''
instance_method - 1
Metodo de instancia também são conhecidos como Bound methods desde que o metodo dentro da classe estão vinculados as da instancia criada da classe, via 'self'.
'''

class A(object):
    def method(*argv):
        return argv


a = A()
print(a.method)
'''
A função 'print()' vai imprimir o seguinte
17.py"
<bound method A.method of <__main__.A object at 0x000001DAFBE816A0>>
A saindo mostra que o 'metodo' é vinculado ao metodo
'''