def som(n):
    s = soma = 0 
    for i in range(1 , num):
        if i <= 1:
            s = i/i
            soma += s

        if i > 1:
            s = i/(1 + 2)
            soma += s
            
    print(f'soma: {soma:.2f}')

num = int(input('Número de termos: '))
x = som(num)