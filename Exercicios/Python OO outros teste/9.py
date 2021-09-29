'''
inheritance - 1
O codigo abaixo mostra como uma classe pode herdar de outra classe.
Nos temos duas classes, 'Date, e 'Time'. Aqui 'Time' herda de 'Date'.
Qualquer classe que herda de outra classe (também chamada de classe parente) herda os metodos e atributos da classe parente.
Portanto, qualquer instancia criada na classe 'Time' pode acessar os metodos definidos na classe parente 'Date'.
'''

class Date(object):
    def get_date(self):
        print('2016-05-14')

class Time(Date):
    def get_time(self):
        print('07:00:00')

'''
Criando uma instancia para 'Date'
'''
dt = Date()
dt.get_date()
'''
Acessando o metodo 'get_date()' de 'Date'
'''
print('-'*12)

'''
Criando a instancia de 'Time'.
'''
tm = Time()
tm.get_time()
'''
Acessando o metodo 'get_time()' de 'Time'.
'''
tm.get_date()
'''
Acessando o 'get_date()' que foi definido na classe parente 'Date'.
'''