#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles
num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num = []
soma = num1

while soma < num2-1:
    soma += 1
    num.append(soma)

print(num)