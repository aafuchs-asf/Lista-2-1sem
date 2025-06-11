#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
fat = []
fat_result = []
result = 1
num = int(input('Digite o número: '))

for i in range (num):
    fat.append(num-i)

for j in range (num):
    result *= fat[j-1]
    fat_result.append(result)
    
print(fat_result[-1],'é o resultado da operação')