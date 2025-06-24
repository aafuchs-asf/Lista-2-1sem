base = int(input('Montar tabuada de: '))
num = []
result = 0
y = True
while y:
    numStart = int(input('Começar por: '))
    numStop = int(input('Terminar por: '))

    if numStop < numStart:
        print('Atenção! O número inicial é maior que o final!')

    else:
        y = False

for i in range (numStart, numStop + 1):
    num.append(i)

print(f'Vou montar a tabuada de {base} começando em {numStart} e terminando em {numStop}:')

for i in range(len(num)):
    result = base * num[i]
    print(f'{base} x {num[i]} = {result}')