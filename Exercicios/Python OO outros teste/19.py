'''
decorators - 1
Decorações são funções que complementam outras funções, em outras palavras, modifica uma função ou metodo.
No exemplo a baixo, nos temos uma função chamada 'decorated'.
Essa função só imprime 'This happened'.
Nos temos uma decoração criada e nomeada 'inner_decorator()'.
Essa função da decoração tem uma função dentro, que faz algumas operações (imprime algumas coisas simples) depois retorna o rotorno do valor da função interna.
Como isso funciona?
A) A função 'decorated()' é chamada.
B) Desde que a decoração '@my_decorator' e definida acima de 'decorated()', 'my_decorator()' é chamada.
C) my_decorator() pega um argumento do nome da função, então portanto 'decorated()' é passado como o argumento.
D) 'my_decorator()' faz o seu trabalho, e quando alcança 'myfunction()' chama a atual função, decorated().
E) Uma vez que a função 'decorated()' esta pronta, retorna para 'my_decorator()'.
F) Portanto, usar um decorador, pode mudar dramaticamente o comportamento de uma função que você estar executando no momento.
'''

def my_decorator(my_function):
    def inner_decorator():
        print('This happened before!')
        my_function()
        print('This happens after')
        print('This happend at the end!')
        return inner_decorator


@my_decorator
def my_decorated():
    print('This happened!')

if __name__ == '__main__':
    my_decorated()

