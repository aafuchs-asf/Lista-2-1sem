#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais
#número ele é divisível.
num = int(input('Digite um número: '))
y = True
w = v = 0
div = []

while y:
    for i in range(num):
        if i != 0 and i != 1:
            w = num%i

            if i != 0 and i != 1:
                w = num%i

                if w == 0:
                    div.append(i)
                    
    if w != 0 and i != 1 and i != 0:
        y = False
        w = 0 

if not div:
    print(num,'é primo')

else:
    print(div)