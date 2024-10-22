dados = {}
pessoas = []
mulheres = []
resp = ''
totidade = 0
while True:
    if resp == 'N':
        break
    dados['Nome'] = str(input('Nome: '))
    dados['Idade'] = int(input('Idade: '))
    totidade += dados['Idade']
    while True:
        sexo = dados['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo not in 'MF':
            print('ERRO! Responda apenas M ou F.')
        else:
            dados['Sexo'] = sexo
            if sexo == 'F':
                mulheres.append(dados['Nome'])
            break
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp not in 'SN':
            print('ERRO! Responda apenas S ou N.')
        else:
            break
print(pessoas)
print('=-' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = float(totidade / len(pessoas))
print(f'B) A média de idade é de {media} anos')
print(f'C) As mulheres cadastradas foram {mulheres}')
print(f'D) Lista de pessoas que estão acima da média: ')
for p in pessoas:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')