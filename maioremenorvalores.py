resposta = 'S'
cont = soma = maior = menor = 0
while resposta == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if n == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
media = soma / cont
print('Você digitpu {} números e a média foi {:.2f}.'.format(cont, media))
