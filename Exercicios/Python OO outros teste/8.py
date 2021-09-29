'''
class-instance-attributes
Este codigo mostra que uma instancia pode acessar os proprios atributos assim como os atributos da classe
Nos temos um atributo de classe chamado 'count' e adicionamos um para cada vez que criamos uma instancia.
Isso pode ajuda a contar o numero de instancias enquanto instanciamos.
'''

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        print(self.val)

    def get_count(self):
        print(InstanceCounter.count)

a = InstanceCounter(5)
b = InstanceCounter(10)
c = InstanceCounter(15)

for obj in (a, b, c):
    print(f'Value of obj: {obj.get_val()}')
    print(f'Count : {obj.get_count()}')