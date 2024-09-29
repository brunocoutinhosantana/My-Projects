from random import randint
numpc = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
num = int(input('Qual o seu palpite? '))
cont = 0
while numpc != num:
    if num > numpc:
        print('Menos... Tente mais uma vez.')
        num = int(input('Qual o seu palpite? '))
    else:
        print('Mais... Tente mais uma vez.')
        num = int(input('Qual o seu palpite? '))
    cont += 1
print('Parabéns, você conseguiu acertar em {} tentativas'.format(cont))
