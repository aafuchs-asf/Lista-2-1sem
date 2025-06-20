# Fatorial de: 5
# 5! = 5 . 4 . 3 . 2 . 1 = 120

fat = []
fatResult = []
result = 1
num = int(input('Digite o número: '))

for i in range (num):
    fat.append(num-i)

for j in range (num):
    result *= fat[j-1]
    fatResult.append(result)

print (fat)
print(fatResult)
    
print('Fatorial de',num)
print(f'{num}! = {fat[0]} {fatResult[-1]}')