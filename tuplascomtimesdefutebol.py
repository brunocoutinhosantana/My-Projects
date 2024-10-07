times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flmanego', 'São Paulo', 'Internacional',
         'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Atlhético-MG', 'Grêmio', 'Criciúma',
         'Bragantino', 'Juventude', 'Athletico-PR', 'Fluminense', 'EC Vitória',
         'Corinthians', 'Cuiabá', 'Athletico-GO')
print('-='*20)
print(f'Lista de times do Brasileirão 2024: {times}')
print('-='*20)
print(f'Os 5 primeiros são: {times[:5]}')
print('-='*20)
print(f'Os quatros últimos são: {times[-4:]}')
print('-='*20)
print(f'Times de forma alfabética: {sorted(times)}')
print('-='*20)
print(f'O {times[7]} está na {times.index("Cruzeiro")+1}ª posição')
