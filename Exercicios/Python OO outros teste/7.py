'''
class-atributes - 2
O codigo a baixo mostra dois pontos importantes:

A) Um atributo de classe pode ser sobescrevido em uma instancia, apesar disso ser ruim quebrar o encapsulamento.
B) Existe um caminho de pesquisar um atributo em python. A primeira coisa é definir o metodo da classe e o acima da classe.
Nos estamos substituindo a 'classy' na instancia do atributo da classe 'dd'. 
Quando é substituido, o interpretador python le o valor substituido.
Porem quando o novo valor é deletado com 'del, o substituido não esta mais presente na instancia, e portanto a pesquisa procura no nivel acima e recebe da classe
'''

class YourClass(object):
    classy = 'class value'

dd = YourClass()
print(dd.classy)
'''
Esse deve retornar a string 'class value'
'''

dd.classy = 'Instance value'
print(dd.classy)
'''
Esse deve retornar a string 'Instance value'
'''
'''
Esse vai deletar o valor setado em 'dd.classy' na instancia.
'''
del dd.classy
'''
Desde que o valor que subsititiu foi apagado, ele ira printar 'class value'.
'''
print(dd.classy)