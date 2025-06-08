n = int(input('Digite o número de termos desejado: '))
fib = []
x = 0

if (len(fib)) == 0:
    fib.append(1)
if fib[0] == 1:
    fib.append(1)

for i in range (n-1):
    if i >= 1:
        x = fib[i-1] + fib[i]
        fib.append(x)
        x = 0

print(fib, len(fib),'termos')