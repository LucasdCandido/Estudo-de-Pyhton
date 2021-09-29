'''
init_constructor - 2
Nos adicionamos um teste no construtor __init__() para checar se o 'value' é ou não é int
'''

class MyNum(object):
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.value = value

    def increment(self):
        self.value += 1
        print(self.value)


a = MyNum(10)
a.increment()
'''
Aqui deve printar 11
'''
a.increment()
'''
Aqui deve printar 12
'''