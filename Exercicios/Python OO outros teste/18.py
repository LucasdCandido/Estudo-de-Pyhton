'''
instance_methods
Metodos de instancia são o caminho normal para acessar os metodos, vistos em todas as classes vistas até agora. por instanciar instancias para a classe, e acessar o metodo dentro da classe. O uso de 'self' é muito importante em metodos de instancia devido ao 'self' sendo um gancho/jeito de lidar com a instancia em si, ou  a instancia por si mesma.
Vamos olhar para um exemplo anterior, mais uma vez, para entender 'metodo de instancia'.
Nos temos o construtor __init__(), e tres metodos dentro da classe 'InstanceCounter'.
Tres instancia a, b e c foram criadas para a classe 'InstanceCounter'.
Desde que o metodo definido na classe são acessados pelas instancias 'a', 'b' e 'c', esses metodos são chamados 'metodos de instancia'.
Desde que a instancia é vinculada com o metodo definido na classe pela palavra-chave 'self', nos também podemos chamar 'metodo de instancia' de 'metodos de vinculos'.
No codigo abaixo, a intancia é 'obj' (o interador) e nos acessamos cada metodo como 'obj.set_val()', and 'obj.get_count'.
'''

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(5)
b = InstanceCounter(10)
c = InstanceCounter(15)

for obj in (a, b, c):
    print(f'Value of object: {obj.get_val}')
    print(f'Count: {obj.get_count}')