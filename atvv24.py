def mediaArit():
    y = True
    soma = ad = 0
    while y:
        x = float(input('Digite o número: '))
        ad += 1
        soma += x
        cond = input('Deseja adicionar outro número(s/n)? ')
        if cond == 'n' or cond =='N':
            y = False
    result = soma/ad
    
    return result
    
a = mediaArit()
print(a,' é a média dos números')