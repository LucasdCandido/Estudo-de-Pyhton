'''

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
c.fetch('frizbee')
d.swatstring()