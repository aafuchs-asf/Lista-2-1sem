#Faça um programa que leia 5 números e informe a soma e a média dos números
num = [1, 3, 7, 35, 21]
s = 0

for i in range (len(num)):
    s += num[i] 
    
print(s,'é a soma')

m = s/len(num)
print(m,'é a média')
