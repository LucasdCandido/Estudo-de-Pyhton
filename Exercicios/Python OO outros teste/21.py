'''
Aqui, a função 'decorated()' recebe um argumento e imprime ele de volta no terminal.
Equanto o decorador '@my_decorator' é chamado, ele recebe a função 'decorated()' como um argumento, e o argumento do 'decorated()' como o argumento de 'inner_decorator()'.
Portanto o argumento 'number' é passado para 'num_copy'
'''

import datetime

def my_decorator(inner):
    def inner_decorator(num_copy):
        print(datetime.datetime.utcnow())
        inner(int(num_copy)+ 1)
        print(datetime.datetime.utcnow())
        return inner_decorator


@my_decorator
def decorated(number):
    print('This happened : ' + str(number))

if __name__ == "__main__":
    decorated(5)