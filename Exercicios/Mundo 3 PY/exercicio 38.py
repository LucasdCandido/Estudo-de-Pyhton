classificação = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Atlético-GO', 'Ceará-SC', 'Internacional', 'Santos', 'Corinthians', 'Juventude', 'Bahia', 'São Paulo', 'Fluminense', 'Cuiabá', 'Sport Recife', 'América-MG', 'Grêmio', 'Chapecoense')
n = c = m = contador = 0
time = ""
print('\n'.join(classificação[:5]))
print('\n'.join(classificação[-4:]))
print(sorted(classificação))
print(classificação.index("Chapecoense")+1)




"""print(f'\nOs primeiros 5 colocados na tabela do Brasileirão são: \n')
while n < 5:
    print(classificação[n])
    n += 1
print(f'\n Os ultimos 4 colocados na tabela do Brasileirão são: \n')
n = 16
while n < 20:
    print(classificação[n])
    n += 1
print(f'\nOs times que atualmente estão na Serie A do Brasileirão em ordem alfabetica são: \n')
while True:
    times = sorted(classificação)
    print(f'{times[c]}'' ', end='')
    c += 1
    if c >= 19:
        break
for m in range(0, len(classificação), 1):
    time = classificação[m]
    contador += 1
    if time == 'Chapecoense':
        break
print(f'\n\nO time Chapecoense esta classificado na posição {contador}!')"""

"""Crie uma tupla preenchida com os 20 primeiros colocados da 
tabelo do campeonato brasileiro de futebol, na ordem de colocação.
Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabetica.
D) Em que posição na tabela esta o time Chapecoense.
"""