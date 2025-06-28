def somaTermo(num):
    h = 0
    divid = 1
    for i in range(1, num + 1):
        h += i/divid
        divid += 2

    print(f'Soma dos termos: {h:.2f}')

x = int(input('Número de termos: '))
y = somaTermo(x)