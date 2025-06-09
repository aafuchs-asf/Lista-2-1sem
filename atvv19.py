#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
num = []
n = True
x = 'a'
soma, med, y = 0, 0, 0

while n:
    y = int(input('Digite um número para o conjunto: '))
    if y >=0 and y <=1000:
        num.append(y)
        x = input('Gostaria de adicionar outro número (s/n)? ')
        if x == 'n' or x =='N':
            n = False
    else:
        print('Digite APENAS números entre 0 e 1000')

for i in range (len(num)):
    soma += num[i]
    
med = soma/len(num)

print(num,'num')
print(soma,' é a soma')
print(med,' é a média')