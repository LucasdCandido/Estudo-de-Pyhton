'''
decorators - 4
Esse exemplo se constroi encima dos exemplos de decorativos anterioes.
O exemplo anterior, mostra como lidar com um argumento passado para uma função.
Esse exemplo mostra como podemos lidar com multplos argumentos.
Lembrete: 'args' é uma lista de argumentos passados, enquanto 'kwargs' é um dicionario de argumentos passados.
'''

def decorator(inner):
    def inner_decorator(*args, **kwargs):
        print(args, kwargs)
    return inner_decorator


@decorator
def decorated(string_args):
    print('This happened : ' + string_args)

if __name__ == '__main__':
    decorated('Hello, how are you?')