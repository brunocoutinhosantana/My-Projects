dados = {}
gols = []
total = 0
time = []
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {dados["Nome"]} jogou? '))
    gols.clear()
    for p in range(1, partidas + 1):
       gols.append(int(input(f'    Quantos gols na partida {p}? ')))
    for g in gols:
       total += g
    dados['Gols'] = gols.copy()
    dados['Total'] = total
    total = 0
    time.append(dados.copy())
    while True:
        res = str(input('Quer continuar? [S/N] ')).upper()[0]
        if res in 'NS':
            break
        print('ERRO! Responda somente S ou N')
    if res == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para encerrar o programa]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i} fez {g} gols.')
    print('-=' * 30)
print()
print('>>> PROGRAMA ENCERRADO <<<')
