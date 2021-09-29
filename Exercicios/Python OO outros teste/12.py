'''
polymorphism - 2
Outro exemplo para Polimorfismo estar atribuidos de varias funções em python. Por exemplo, a função construtora chamada 'len'.
'len' é ultilizavel em praticamente todos os tipos, tais como string, ints, floats, dictionaries, lists, tuples etc...
Quando len é chamado para um tipo, na verdade é chamado função privada 'len' para o tipo ou __len__
Todo tipo de objeto que tem suporte para 'len' vai ter o construtor de função privada 'len'.
Portanto, por exemplo, o tipo lista já tem um função construtor 'len' do python code, e quando você roda a função len() nesse tipo de dado, vai checar se a função privada len é ou não valida para esse tipo de dado.
Se for valida, ela vai rodar.
'''

text = ['Hello', 'Hola', 'helo']
print(len(text))

print(len('Hello'))
print(len({'a':1,'b':2, 'c':3}))