def analisador(*num):
    print('=-' * 30)
    print('Analisando os valores passados . . .')
    for n in num:
        print(f'{n}',  end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}.')


analisador(2, 9, 4, 5, 7, 1)
analisador(4, 7, 0)
analisador(1, 2)
analisador(6)
analisador()
