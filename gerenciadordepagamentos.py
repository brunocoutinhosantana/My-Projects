print('='*12+' LOJAS COUTINHO '+'='*12)
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/ cheque
{ 2 ] à vista cartão
[ 3 ] 2x no cartão'
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    print('Sua compra no valor de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco - (preco*10/100)))
elif opcao == 2:
    print('Sua compra no valor de R${:.2f} vai custar R${:.2f} no final'.format(preco, preco - (preco*5/100)))
elif opcao == 3:
    print('Sua compra de R${:.2f} parceladas em 2x de R${:.2f}'.format(preco, preco/2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra de R${:.2f} parcelada em {}x de R${:.2f} COM JUROS'.format(preco, parcelas, (preco+(preco*20/100))/parcelas))
    print('A sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, preco+(preco*20/100)))
else:
    print('OPÇÃO INVÁLIDA DE PGAMENTO')
    