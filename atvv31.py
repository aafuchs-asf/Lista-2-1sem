def calcRegistrador():
    prod = []
    val = []
    y = True
    a = soma = 0
    
    while y:
        x = float(input('Insira o valor do produto: '))
        if x > 0:
            val.append(x)
            a += 1
            prod.append(a)

        else:
            y = False

    print('Lojas Tabajara')
    for i in range (len(prod) + 1):
        if i >= 1:
            print(f'Produto {i}: R${val[i-1]}')

    print(f'Produto {prod[-1] + 1}: R$0')

    for y in range(len(val)):
        soma += val[y]

    print(f'Total: R${soma}')
          
    din = float(input('Pagamento (R$): '))
    print(f'Troco: R${din - soma}')

a = input('Caixa Registradora (s/n): ')
if a == 's' or a == 'S':
    calcRegistrador()