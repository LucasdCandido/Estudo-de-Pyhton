from classes4 import *

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

c1 = Cliente('Luiz', 45)
c1.comprar()
c1.falar()

a1 = Aluno('Maria', 54)
a1.falar()
a1.estudar()

p1 = Pessoa('João', 43)
p1.falar()