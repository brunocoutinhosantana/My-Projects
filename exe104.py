def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return num
            break
        else:
            print('ERRO! Digite um número inteiro válido.')


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
