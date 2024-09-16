peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / altura**2
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc <= 24.9:
    print('Você está no peso normal!')
elif 24.9 < imc <= 29.9:
    print('Você está com excesso de sobrepeso!')
elif 30 <= imc <= 40:
    print('Você está obeso!')
else:
    print('você está com obesidade mórbita!')