#Altere o programa anterior para mostrar no final a soma dos números
num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num = []
soma = num1
add = 0

while soma < num2-1:
    soma += 1
    num.append(soma)

for i in range(len(num)):
    add += num[i]

print(add,' é a soma')