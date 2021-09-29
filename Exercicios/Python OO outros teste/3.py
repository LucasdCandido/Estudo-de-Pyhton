'''
Encapsulamento - 3
Aqui nos vemos outro exemplo, nele temos 3 metodos, set_val(), get_val() e increment_val().
set_val() ajuda a colocar um valor, get_value() printa o valor, e increment_val() aumenta o valor em 1.
Nos ainda podemos quebrar o encapsulamento aqui chamando 'self.value' diretamento a instancia, o que é uma pratica ruim.
set_val() nos força a colocar um numero inteiro, o que o codigo precisa para funcionar perfeitamente. Aqui, é possivel quebrar o encapsulamento chamando 'self.val' diretamento, o que causa resultados inesperados depois. 
Neste exemplo, o codigo é escrito para forçar a entrada de um numero inteiro, se nos não quebrarmos o encapsulamento e ir através do 'set_val()'
'''

class MyInteger(object):
    def set_value(self,val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        print(self.val)

    def increment_val(self):
        self.val += 1
        print(self.val)

a = MyInteger()
a.set_value(10)
a.get_val()
a.increment_val()
print('\n')

'''
Tentando quebrar o encapsulamento em uma nova instancia com um int
'''
c = MyInteger()
c.val = 15
c.get_val()
c.increment_val()
print('\n')

'''
Tentando quebrar o encapsulamento com uma nova instancia str
'''
b = MyInteger()
b.val = 'MyString'
'''
Quebrando o encapsulamento, funciona perfeitamento
'''
b.get_val()
'''
Imprime o val setado pela quebra do encapsulamento
'''
b.increment_val()
'''
Aqui vai falhar, já que str + int não funciona
'''
print('\n')
