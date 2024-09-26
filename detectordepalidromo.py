frase = str(input('Digite uma frase: ').replace(' ', '').upper())
print('O contrário da frase {} é {}'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('A frase digitade é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
