boletin = {}
boletin['nome'] = str(input('Nome: '))
boletin['media'] = float(input(f'Média do {boletin["nome"]}: '))
if boletin['media'] >= 7:
    boletin['situacao'] = 'Aprovado'
elif 7 > boletin['media'] >= 5:
    boletin['situacao'] = 'Recuperação'
else:
    boletin['situacao'] = 'Reprovado'
print('=-' * 30)
for k, v in boletin.items():
    print(f'- {k} é igual a {v}')
