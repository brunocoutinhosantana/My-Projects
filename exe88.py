from random import randint
from time import sleep
print('-'*30)
print('JOGO NA MEGA SENA')
print('-'*30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {jogos} jogos')
sleep(1)
sorteados = []
numeros = []
for j in range(0, jogos):
    for n in range(0, 6):
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
    sorteados = numeros[:]
    numeros.clear()
    print(f'Jogo {j + 1}: {sorted(sorteados)}')
