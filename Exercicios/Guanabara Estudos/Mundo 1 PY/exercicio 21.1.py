def contar_letrar(frase):
    print(f'Na frase digitada foram encontradas {frase.count("a")} letras "A"\nA primeira vez que a letra "A" aparece na frase é {frase.find("a")}\nE a ultima vez que a letra "A" aparece na frase é {frase.rfind("a")}')


frase = input('Digite uma frase: ').lower().strip()
contar_letrar(frase)