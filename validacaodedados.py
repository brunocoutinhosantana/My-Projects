c = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while c != 'M' and c != 'F':
    c = str(input('Dados inválidos. Pro favor, informe seu sexo: ')).upper()
if c == 'M':
    print('Sexo masculino cadastrado com sucesso!')
else:
    print('Sexo feminino cadastrado com sucesso!')
