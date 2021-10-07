def nome_cidade(cidade):
    nome = cidade.split()[0]
    print(f'Vamos descobrir de sua cidade começa com "Santo": {"santo" in nome.lower()}')


cidade = input('Digite o nome da sua cidade: ')
nome_cidade(cidade)