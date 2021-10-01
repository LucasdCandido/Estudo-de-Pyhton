def salario(dinheiro):
    salario_final = dinheiro * (1 + (15/100))
    print(f'O valor do salario com aumento de 15% fica RS {salario_final:.2f}')

dinheiro = float(input('Digite o valor do salario do funcionario: RS '))
salario(dinheiro)