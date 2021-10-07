def primeiro_ultimo(nome):
    primeiro = nome[0]
    ultimo = nome[len(nome)-1]
    print(f'Seu primeiro nome é {primeiro}\nSeu ultimo nome é {ultimo.capitalize()}')


nome = input('Digite seu nome completo: ').capitalize().strip().split()
primeiro_ultimo(nome)