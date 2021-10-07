from random import randint

def jogada_maquina():
    random = randint(0,10)
    print(random)

def jogada_jogador(jogada):
    resultado = ""
    if jogada == jogada_maquina:
        resultado = ('Vitoria!')
    else:
        resultado = ('Derrota!')
    print(jogada_maquina)
    return resultado

print(
    '''
    Seja bem vindo ao nosso jogo!
    Aqui vamos jogar uma partida para adivinhar qual o numero a maquina escolheu, você tem 5 chances de conseguir até a maquina chegar ao final das chances de você acertar qual numero ela escolheu!
    '''
)
jogada = int(input('Digite um numero entre 0 e 10: '))
jogada_jogador(jogada)