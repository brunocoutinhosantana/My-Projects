from time import sleep


def contagem(inicio, fim, passo):
    print('=-' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if passo < 0:
        passo *= -1
    c = inicio
    if inicio < fim:
        while c <= fim:
            print(f'{c}', end=' ')
            c += passo
            sleep(0.7)
        print('FIM!')
    else:
        while c >= fim:
            print(f'{c}', end=' ')
            c -= passo
            sleep(0.7)
        print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('=-' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contagem(i, f, p)
