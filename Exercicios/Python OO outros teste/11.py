'''
polymorphism - 1
Polimorfismo quer dizer ter a mesma interface/atributo em diferentes classes.
Polimorfismo tem a caracteristica de ser possivel atribuir diferentes contextos.
Um não-tão-claro/claro exemplo é, diferentes classes tem funções com o mesmo nome.
Aqui, as classes Dog e Cat tem o mesmo nome de metodo 'show_affection'.
Mesmo que os dois sejam iguais, os dois tem ações diferentes na instancia.
Desde que a ordem de pesquisa é 'instance'->'class'->'parent class', mesmo se a 'class' e a 'parent class' tem os mesmo nomes de funções, a instancia vai sempre escolher a primeira, da 'class' e não vai para a 'parent class'.
'''

class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name} eats {food}')

    
class Dog(Animal):
    def fetch(self, thing):
        print(f'{self.name} goes after the {thing}')

    def show_affection(self):
        print(f'{self.name} wags tail')

    
class Cat(Animal):
    def swatstring(self):
        print(f'{self.name} shreds more string')

    def show_affection(self):
        print(f'{self.name} purrs')


for a in (Dog('Rover'), Cat('Fluffy'), Cat('Lucky'), Dog('Scout')):
    a.show_affection()