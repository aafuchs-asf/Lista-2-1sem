base = int(input('Digite o número que deseja para a tabuada: '))
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for i in range(len(num)):
    soma = base * num[i]
    print(f'{base} x {num[i]} = {soma}')