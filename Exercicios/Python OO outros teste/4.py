'''
init_contructor - 1
__init__() é um metodo construtor que nos ajuda a setar valores iniciais enquanto instancia a classe.
__init__() vai ser chamado com os atributos setados em __init__(), enquanto a classe é instanciada.
O '__' antes e depois do nome do metodo denota que esse é um metodo privado. É chamado de privado ou metodo magico desde que é chamado internamente ou automaticamente.
'''

class MyNum(object):
    def __init__(self):
        print('Chamando o construtor __init__ ! \n')
        self.val = 0

    def increment(self):
        self.val += 1
        print(self.val)

dd = MyNum()
dd.increment()
dd.increment()