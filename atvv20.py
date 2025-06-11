#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
#fatorial a números inteiros positivos e menores que 16.
fat = []
fat_result = []
result, num = 1, 0
w = True

while w:
    num = int(input('Digite o número: '))
    for i in range (num):
        fat.append(num-i)

    for j in range (num):
        result *= fat[j-1]

    if result < 16:
        fat_result.append(result)
        print(f'O resultado da operação é: {result}')

    else:
        print('Resultado maior que 16!')

    y = (input('Deseja tentar novamente? (s/n): '))

    if y !='s' or y != 'S':
        w = False
    
    elif y == 's' or y == 'S':
        num, result= 0, 1
        fat.clear()
        fat_result.clear()