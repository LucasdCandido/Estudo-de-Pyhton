'''
class-atributes - 1
Aqui vamos definir os atributos da classe 'YourClass' enquanto atribuimos com a função.
O atributo definido na classe é chamado 'class atributes' e o atributo definido na função é chamado 'instance attributes'
'''

class YourClass(object):
    classy = 10

    def set_value(self):
        self.insty = 100


dd = YourClass()
dd.classy
'''
Esse vai buscar o atributo 10.
'''
dd.set_value()
dd.insty
'''
Esse vai buscar o atributo da instancia 100.
'''

'''
Uma vez que 'dd' é instanciado, nos podemos acessar os dois classe e instancia atributos, dd.classy e dd.insty
'''