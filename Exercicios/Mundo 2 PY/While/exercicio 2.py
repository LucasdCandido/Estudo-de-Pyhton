nome = str(input('digite seu nome: ')).upper().strip()
senha = str(input('Digite sua senha: ')).upper().strip()
while nome == senha:
    print('A senha deve ser diferente do nome! ')
    senha = str(input('Digite uma senha diferente: ')).upper().strip()
print('Parabéns {}! Cadastro efetuado com sucesso!'.format(nome))

"""Crie um programa que faça uma validação de usario e senha e só aceite
uma senha que seja diferente do nome de usuario
"""