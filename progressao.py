print('=+='*10)
print('Gerador de PA')
print('=+='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input(('Razão de PA: ')))
cont = 1
total = 0
mais = 10
while mais !=0:
    total += mais
    while cont <= total:
        print('{} -> '.format(primeiro), end='')
        primeiro += razão
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mai? '))
print('Progressão finalizada com {} termos mostrados'.format(total))