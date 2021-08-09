frase1 = str(input('Digite uma frase: ')).strip()
frase2 = str(input('Digite uma frase: ')).strip()
fra1 = frase1.replace(" ","")
fra2 = frase2.replace(" ","")
cont1 = len(fra1)
cont2 = len(fra2)

print('A frase {}, contem {} caracteres!'.format(frase2, cont1))
print('A frase {}, contem {} caracteres!'.format(frase2, cont2))

if fra1 == fra2:
    print('As frases são iguais!')
else:
    print('As frases são diferentes!')