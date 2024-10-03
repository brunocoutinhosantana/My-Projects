while True:
    num = int(input('Você quer ver a tabuada de qual número? '))
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
