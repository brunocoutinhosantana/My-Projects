lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    res = 'SNsn'
    while res not in 'SsNn':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res == 'N':
        break
print('+='*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print('O valor 5 não foi encontrado na lista!')
else:
    print('O valor 5 foi encontrado na lista!')
