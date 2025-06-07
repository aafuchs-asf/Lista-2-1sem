num = []
soma_par = soma_impar = 0

num.append(int(input('Digite o 1° número: ')))
num.append(int(input('Digite o 2° número: ')))
num.append(int(input('Digite o 3° número: ')))
num.append(int(input('Digite o 4° número: ')))
num.append(int(input('Digite o 5° número: ')))
num.append(int(input('Digite o 6° número: ')))
num.append(int(input('Digite o 7° número: ')))
num.append(int(input('Digite o 8° número: ')))
num.append(int(input('Digite o 9° número: ')))
num.append(int(input('Digite o 10° número: ')))

for i in range (len(num)):
    if num[i]%2 == 0:
        soma_par += 1
    else:
        soma_impar += 1
print(f' Há {soma_par} números pares e {soma_impar} números ímpares')