class Produto:
    def __init__(self, nome, valor, desconto):
        self.nome = nome
        self.valor = valor
        self.desc = desconto

    def valor_desconto(self):
        valor_desc = self.valor - (self.valor * (1+(self.desc/100)))
        valor_final = self.valor + valor_desc
        return valor_final



nome = input('Digite o nome do produto: ')
valor = float(input('Digite o valor do produto: '))
desconto = float(input('Digite a porcentagem do desconto: '))
p1 = Produto(nome, valor, desconto)
print(p1.nome, p1.valor_desconto())