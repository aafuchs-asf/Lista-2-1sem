#A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série
#até que o valor seja maior que 500.
#if i >= 1:
n = int(input('Digite o número de termos desejado: '))
fib = []
x = 0

if (len(fib)) == 0:
    fib.append(1)
if fib[0] == 1:
    fib.append(1)

for i in range (n-2):
    x = fib[-1] + fib[-2]  
        
    if fib[-1] > 500:
       print('Enecerrando a sequência, pois o último termo é maior que 500')
       break

    else:
        fib.append(x)
        
print(fib, len(fib),'termos')