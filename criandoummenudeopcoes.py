v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
print('=-='*10)
opcao = 0
while opcao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        res = v1 + v2
        print('A soma entre {} e {} é igual a {}'.format(v1, v2, res))
        print('=-=' * 10)
    elif opcao == 2:
        res = v1 * v2
        print('A multiplicação entre {} e {} é igual a {}'.format(v1, v2, res))
        print('=-=' * 10)
    elif opcao == 3:
        if v1 > v2:
            print('O maior número digitado foi {}'.format(v1))
            print('=-=' * 10)
        elif v1 < v2:
            print('O maior número digitado foi {}'.format(v2))
            print('=-=' * 10)
        else:
            print('Os 2 valores digitados são iguais')
            print('=-=' * 10)
    elif opcao == 4:
        print('Digite novamente')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    else:
        print('Opção Inválida, tente novamente!!')
print('Você saiu do programa!!')