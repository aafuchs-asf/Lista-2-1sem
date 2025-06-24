listCit = []
cod = numV = numA = sV = sA = medV = medA = l = medAA = sAA= 0
for i in range (5):
    cod = int(input('Código da cidade: '))
    numV = int(input('Número total de carros: '))
    numA = int(input('Número total de acidentes: '))

    listCit.append([cod, numV, numA])

meA = listCit[0]
mA = listCit[0]

for p in listCit:
    if p[2] > mA[2]:
        mA = p
    if p[2] < meA[2]:
        meA = p

for j in listCit:
    sV += j[1]

medV = sV/5

for w in listCit:
    sA += j[2]

medA = sA/5

for k in listCit:
    if k[1] < 2000:
        sAA += j[2]
        l += 1

medAA = sAA/l

print(f'Menos acidentes: {meA}')
print(f'Mais acidentes: {mA}')
print(f'Média de veiculos: {medV}')
print(f'Média de acidentes: {medA}')