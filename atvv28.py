# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor
# médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para cada um.
cd = int(input('Digite a quantidade de CDs: '))
valTotal = 0

for i in range (cd):
    val = float(input('Digite o valor do CD: '))
    valTotal += val

x = valTotal/cd
print(f'A média do valor por CD foi R${x} e no total foram investidos R${valTotal}.')