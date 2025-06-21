fat = []
fatResult = []
result = 1
elem = ''
num = int(input('Digite o número: '))

for i in range (num):
    fat.append(num-i)

    if i != 0:
        elem += f'{num -i}'
        elem += '.'

for j in range (num):
    result *= fat[j-1]
    fatResult.append(result)
        
print('Fatorial de',num)
print(f'{num}! = {num}.{elem} = {fatResult[-1]}')