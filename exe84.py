valores = [[], []]
for v in range(0, 7):
    value = int(input(f'Digite o {v+1}º valor: '))
    if value % 2 == 0:
        valores[0].append(value)
    else:
        valores[1].append(value)
print('=-'*30)
print(f'O valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram {sorted(valores[1])}')
