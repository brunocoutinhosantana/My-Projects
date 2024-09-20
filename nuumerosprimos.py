s = 0
num = int(input('Digite um número inteiro: '))
for c in range(1, num + 1):
    if num % c == 0:
        s += 1
print('O número {} foi divisível {} vezes'.format(num, s))
if s == 2:
    print('O número {} é um número primo'.format(num))
else:
    print('e por isso ele NÃO é um número primo!')

