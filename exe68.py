from random import randint
print('=-'*13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*13)
cont = 0
while True:
    n = int(input('Diga um valor: '))
    j = ' '
    while j not in 'PI':
        j = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    pc = randint(0, 10)
    tot = n + pc
    if tot %2 == 0:
        res = 'PAR'
    else:
        res = 'IMPAR'
    print(f'Você jogou {n} e o computador {pc}. Total de {tot} DEU {res}')
    if j == res[0]:
        print('Você VENCEU!')
        cont += 1
        print('Vamos jogar novamente...')
    else:
        print(f'GAME OVER você venceu {cont} vezes')
        break
