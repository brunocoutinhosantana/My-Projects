lista = []
listapar = []
listaimpar = []
while True:
    value = int(input('Digite um número: '))
    lista.append(value)
    if value % 2 == 0:
        listapar.append(value)
    else:
        listaimpar.append(value)
    res = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if res == 'N':
        break
print(f'A lista de valore digitados fo {lista}')
print(f"Os valores pares digitados foram {listapar}")
print(f'Os valores ímpares digitados foram {listaimpar}')
