from classes2 import CarrinhoDeCompra
from classes2 import Produto

carrinho = CarrinhoDeCompra()
p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)

carrinho.lista_produto()
print(carrinho.soma_total())