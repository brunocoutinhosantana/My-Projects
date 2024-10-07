lista = (int(input('Digite um número: ')),
            int(input('Digite outro número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite o último número: ')))
print(f'Você digitou os valores {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
for c in lista:
    if c% 2 ==0:
        print(f'Os valores pares digitados foram: {c}', end=' ')
