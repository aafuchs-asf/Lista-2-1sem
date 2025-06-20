def tabelaPao(qtd, prc):
    w = 0
    print('Panificadora Pão de Ontem - Tabela de preços')
    for i in range (qtd + 1):
        if i != 0:
            w += prc
            print(f'{i} - R$ {w:.2f}')

inic = input('Tabela de preços (s/n): ')

if inic == 's' or inic == 'S':
    x = float(input('Insira o valor por pão: '))
    y = int(input('Insira a quantidade de pães: '))
    inic = tabelaPao(y, x)