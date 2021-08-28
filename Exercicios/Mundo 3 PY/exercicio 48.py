contador = 0
expressao = input('Digite uma frase com parenteses: ').upper().strip()
for e in expressao:
    if expressao == '(':
        contador += 1
    else:
        contador -= 1
    if contador < 0:
        break
if contador == 0:
    print('Expressão valida!')
else:
    print('Expressão invalida!')   



"""Contrua um programa onde o usuario digita uma expressão qualquer que usa parenses.
Seu aplicativo devera analisar se a expressão passada esta com os parenteses abertos e fechados na ordem correta.
"""