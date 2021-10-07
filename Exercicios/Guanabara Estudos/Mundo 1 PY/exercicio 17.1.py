def nome_completo(nome):
    total = nome.replace(' ','')
    print(f'A contagem total de letras do seu nome é {len(total)}\nO seu nome todo em maiusculo fica {nome.upper()}\nO seu nome todo em minusculo fica {nome.lower()}\nSeu primeiro nome tem {nome.find(" ")} letras.')

nome = input('Digite seu nome completo: ').strip()
nome_completo(nome)