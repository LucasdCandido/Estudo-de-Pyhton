''''
Encapsulamento - 2
Esse exemplo se baseia encima do exemplo 'Encapsulamento - 1'.
Aqui vemos como podemos atribuir valores em um metodo sem ir pelo metodo proprio, como nos quebramos o encapsulamento.
NOTA: Quebrar o encapsulamento é muito ruim
'''

class MyClass(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        print(self.value)

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(1000)
a.value = 100
'''
<== Sobescrevendo diretamento o 'set_value'
<== Quebrando o encapsulamento
'''


a.get_val()
b.get_val()