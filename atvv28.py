cd = int(input('Digite a quantidade de CDs: '))
valTotal = 0

for i in range (cd):
    val = float(input('Digite o valor do CD: '))
    valTotal += val

x = valTotal/cd
print(f'A média do valor por CD foi R${x} e no total foram investidos R${valTotal}.')