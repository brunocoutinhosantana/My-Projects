r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
    if r1 != r2 != r3 != r1:
        print('Com esses seguimentos, formam um triângulo ESCALENO')
    elif r1 == r2 == r3:
        print('Com esses seguimentos formam um triângulo EQUILÁTERO')
    else:
        print('Com esses seguimentos formam um triângulo ISÓCELES')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triangulo!')
