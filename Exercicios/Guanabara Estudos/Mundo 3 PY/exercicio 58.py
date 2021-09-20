jogador = {}
classificacao = {}
gols = jogos = placar = 0
resposta = ""
while True:
    jogador['Nome'] = input('Qual o nome do jogador? ').upper().strip()
    jogos = int(input(f'Quantos jogos o {jogador["Nome"]} jogou? '))
    jogador['Jogos'] = jogos
    n = 0
    for j in  range(0, jogos):
        gols = int(input(f'Quantos gols ele marcou na partida {j+1}: '))
        jogador['Gols'] = gols
        placar += gols
    jogador['Placar'] = placar
    classificacao['Jogadores'] = jogador.copy()
    reposta = input('Gostaria de cadastrar outro jogador? [S/N] ').upper().strip()[0]
    if resposta in 'N':
        break
for c, l in classificacao.items():
    print(l)


"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai
ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de de gols
feitos em cada partida. No final, tudo isso sera guardado em um dicionario, incluindo o total de 
gols feitos durante o campeonato.
"""