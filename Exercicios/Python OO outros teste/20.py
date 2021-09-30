'''
decorators - 2
Pega esse fragmento do codigo anterior como exemplo, e adiciona um pouco mais de informação a saida.
'''

import datetime

def my_decorator(inner):
    def inner_decorator():
        print(datetime.datetime.utcnow())
        inner()
        print(datetime.datetime.utcnow())
        return inner_decorator


@my_decorator
def decorator():
    print('This happened!')

if __name__ == "__main__":
    decorator()