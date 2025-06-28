def somaTermo(num):
    h = 0
    for i in range(1, num + 1):
        h += 1/i

    print(f'Soma dos termos: {h:.2f}')

x = int(input('Número de termos: '))
y = somaTermo(x)