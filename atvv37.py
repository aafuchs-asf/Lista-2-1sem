y = True
listKg = []
listCm = []
listCod = []
somaKg = somaCm = meC = meK = mC = mK = 0 
while y:
    cod = int(input('Insira o código: '))
    if cod == 0:
        y = False

    else:
        kg = float(input('insira o peso (kg): '))
        listKg.append(kg)
        somaKg += kg
        cm = int(input('Insira a altura (cm): '))
        listCm.append(cm)
        somaCm += cm

        listCod.append(cod)

maiorKg = listKg[0]
menorKg = listKg[0]

for i in range(len(listKg)):
    if listKg[i] > maiorKg:
        maiorKg = listKg[i]
        mK = i
    if listKg[i] < menorKg:
        menorKg = listKg[i]
        meK = i

maiorCm = listCm[0] 
menorCm = listCm[0]

for p in range(len(listCm)):
    if listCm[p] > maiorCm:
        maiorCm = listCm[p]
        mC = p
    if listCm[p] < menorCm:
        menorCm = listCm[p]
        meC = p

codmC = listCod[mC]
codmeC = listCod[meC]
codmK = listCod[mK]
codmeK = listCod[meK]

    
medKg = print(f'Média dos pesos: {somaKg/len(listKg)}Kg')
medCm = print(f'Média das alturas: {somaCm/len(listCm)}cm')
maiorCm = print(f'Maior altura: {maiorCm}. Código {codmC}.')
menorCm = print(f'Menor altura: {menorCm}. Código {codmeC}')
maiorKg = print(f'Mais gordo: {maiorKg}. Código {codmK}')
menorKg = print(f'Mais magro: {menorKg}. Código {codmeK}')