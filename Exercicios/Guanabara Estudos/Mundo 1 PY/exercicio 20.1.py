def encontrar_nome(nome):
    print(f'No seu nome tem "Silva"? : {"silva" in nome.lower()}')

nome = input('Digite seu nome: ').strip()
encontrar_nome(nome)