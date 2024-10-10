lista = []
while True:
    value = int(input('Digite um valor: '))
    if value not in lista:
        lista.append(value)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res in 'N':
        break
print(f'Você digitou os valores {sorted(lista)}')
