dados = {}
gols = []
total = 0
dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {dados["Nome"]} jogou? '))
for p in range(1, partidas + 1):
   gols.append(int(input(f'    Quantos gols na partida {p}? ')))
for g in gols:
   total += g
dados['Gols'] = gols.copy()
dados['Total'] = total
print('-=' *30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
   print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou em {partidas} partidas.')
for p in range(0, partidas):
   print(f'   ==> Na partida {p + 1}, fez {gols[p]} gols.')
print(f'Foi um total de {total} gols')
