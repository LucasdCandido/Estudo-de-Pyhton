'''
inheritance - 2
O codigo abaixo mostra outro exemplo de henrança Dog e Cat são duas classes que herdaram de Animal.
Tanto a instancia criada por Dog ou Cat podem acessar os metodos da classe Animal, eat().
A instancia de 'Dog" pode acessar os metodos de classe e de sua classe parente 'Animal'.
A instancia de 'Cat' pode acessar os metodos de classe e de sua classe parente 'Animal'.
Porem a instnacia criada de 'Cat' não pode acessar os atributos da classe 'Dog', e vice versa.
'''

class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name} is eating {food}')

class Dog(Animal):
    def fetch(self, thing):
        print(f'{self.name} goes after the {thing}')

class Cat(Animal):
    def swatstring(self):
        print(f'{self.name} shred the string!')

d = Dog('Roger')
c = Cat('Fluffy')

d.fetch('paper')
d.eat('dog food')
print('-'*12)
c.eat('cat food')
c.swatstring()

'''
O metodo abaixo vai falhar, desde que a instancia não tem acesso as outras classes.
'''
c.fetch('frizbee')
d.swatstring()