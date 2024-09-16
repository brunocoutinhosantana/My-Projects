from datetime import date
ano = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Atleta categoria: MIRIM')
elif 14 <=idade > 9:
    print('Atleta categoria: INFANTIL')
elif 19 <=idade > 14:
    print('Atleta categoria: JUNIOR')
elif 25 <=idade > 19:
    print('Atleta categoria: SENIOR')
else:
    print('Atleta categoria: MASTER')
