from random import randint
from time import sleep
lista = []


def sorteador():
    c = 0
    print('Sorteando 5 valores da lista:', end=' ')
    while c < 5:
        lista.append(randint(0, 10))
        c += 1
    for a in lista:
        print(f'{a}', end=' ')
        sleep(0.3)
    print('PRONTO!')


def analisador():
    tot = 0
    for v in lista:
        if v % 2 == 0:
            tot += v
    print(f'Somando os valores pares de {lista}, temos {tot}')


sorteador()
analisador()
