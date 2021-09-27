class Compra:
    def __init__(self):
        self.produto = []

    def inserir_produto(self, produto):
        self.produto.append(produto)

    def lista_produtos(self):
        for produto in self.produto:
            print(produto.nome,produto.valor, produto.desconto)

    def valor_final_produto(self):
        for produto in self.produto:
            desconto = float((1+(produto.desconto/100))*produto.valor)
        return produto.nome, desconto

    


class Produto:
    def __init__(self, nome, valor, desconto):
        self.nome = nome
        self.valor = valor
        self.desconto = desconto


compra = Compra
p1 = Produto(nome, )