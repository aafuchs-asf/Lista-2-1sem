listNum = []
num = sA = sB = sC = sD = 0
while True:
    num = int(input('Número: '))

    if num < 0:
        break

    else:
        listNum.append(num)
    print(listNum)

for i in range (len(listNum)):
    if listNum[i] < 25:
        sA += 1
    elif listNum[i] > 26 and listNum[i] < 50:
        sB += 1
    elif listNum[i] > 51 and listNum[i] < 75:
        sC += 1
    elif listNum[i] > 76 and listNum[i] < 100:
        sD += 1

print(f'Números no intervalo[0-25]: {sA}')
print(f'Números no intervalo[26-50]: {sB}')
print(f'Números no intervalo[51-75]: {sC}')
print(f'Números no intervalo[76-100]: {sD}')