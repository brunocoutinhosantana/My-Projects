numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorse', 'Quinze', 'Desesseis', 'Desessete', 'Desoito', 'Desenove', 'Vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num]}')
        break
    else:
        print('Tente novamente!', end=' ')