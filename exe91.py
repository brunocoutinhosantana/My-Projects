from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['Carteira de Trabalho'] = int(input('Cartera de Trabalho (0 não tem): '))
if dados['Carteira de Trabalho'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['idade'] + ((dados['Ano de Contratação'] + 35) - datetime.now().year)
print('=-' * 30)
print(dados)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
