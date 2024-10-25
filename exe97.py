def escreva(txt):
    tamanho = len(txt) + 4
    print('^' * tamanho)
    print(f'  {txt}')
    print('^' * tamanho)


txt = str(input('Digite um texto: '))
escreva(txt)
