soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para para): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} números e a soma dele é {soma}')
