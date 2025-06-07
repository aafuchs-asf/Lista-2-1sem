#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50
y = 0
num = []
impar = []

while y < 50:
    y += 1
    num.append(y)
    
for i in range (len(num)):

    if num[i]%2 != 0:
        impar.append(num[i])
print(impar,': números ímpares entre 1 e 50')


