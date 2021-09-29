"""
Encapsulamento - 1
Encapsulamento serve para preservar os dados da classe usando metodos.
Aqui, nos vamos setar o atributo 'val' atraves do 'set_val()'.
Veja o proximo exemplo, 'Encapsulamento - 2' para mais informação.

Neste exemplo, nos temos dois metodos, 'set_val()' e 'get_val()'
O primeiro agrega a o valor em 'val' enquanto o segundo printa/retorna o valor.
"""

class MyClass(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        print(self.value)
        return self.value

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)

a.get_val()
b.get_val()

"""
NOTA: Se você rodar esse codigo, ele não vai printar nada na tela.
Isso é por que, mesmo se nos chamarmos 'a.get_val()' e 'b.get_val()', a função 'get_val()' não contem a função 'print()'.
Se nos queremos ter a sainda impressa na tela, nos temos que fazer alguma das coisas a seguir:

A) Ou substituir 'return self.value' por 'print(self.value)' ou adicionar o atributo da função print acima de 'return' como 'print(self.value)'
B) Remover 'return(self.value)' e substituir por 'print(self.value)'
"""