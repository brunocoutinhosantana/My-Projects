from datetime import datetime
maior = 0
menor = 0
for c in range(1, 8):
    pessoa = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(c)))
    idade = datetime.now().year - pessoa
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print("No total sao {} pessoas maiores e {} pessoas menores!".format(maior, menor))
