print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = termo +(10 - 1) * razão
for c in range(termo, decimo + razão, razão):
    print('{} -> '.format(c), end =' ')
print('ACABOU')
