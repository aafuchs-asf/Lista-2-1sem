y = True
listTemp = []
soma = 0

while y:
    temp = float(input('Insira a temperatura: '))
    listTemp.append(temp)
    soma += temp

    b = input('Desenha adicionar nova temperatura (s/n): ')
    if b == 'N' or b == 'n':
        y = False

maior = listTemp[0]
menor = listTemp[0]

for i in range (len(listTemp)):
    if listTemp[i] < menor:
        menor = listTemp[i]

    if listTemp[i] > maior:
        maior = listTemp[i]
        
med = soma/len(listTemp)

print(f'Maior temperatura: {maior}')
print(f'Menor temperatura: {menor}')
print(f'Média das temperaturas: {med:.2f}')