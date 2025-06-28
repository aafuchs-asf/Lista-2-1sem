num = input('Número: ')
b = c = ''

for i in range(len(num) - 1, -1, -1):
    b = num[i]
    c += b
    print(f'{c}')
