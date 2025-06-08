num = []
n = True
x = 'a'
soma, med = 0, 0
while n:
    num.append(int(input('Digite um número para o conjunto: ')))
    x = input('Gostaria de adicionar outro número (s/n)? ')
    if x == 'n' or x =='N':
        n = False

for i in range (len(num)):
    soma += num[i]
    
med = soma/len(num)

print(num,'num')
print(soma,' é a soma')
print(med,' é a média')