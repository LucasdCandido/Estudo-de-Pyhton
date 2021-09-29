'''
inheriting-init-constructor
Esse é um exemplo de herança normal que vai construir o proximo exemplo. Tenha certeza de ler e compreender o proximo exemplo.
'''

class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def fetch(self, thing):
        print(f'{self.name} goes after the {thing}')


d = Dog('Roger')
print("The dog's name is", d.name)
d.fetch('frizbee')