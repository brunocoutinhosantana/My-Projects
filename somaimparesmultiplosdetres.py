cont = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('A soma entre todos os {} números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500 é {}!!!'.format(cont, s))


