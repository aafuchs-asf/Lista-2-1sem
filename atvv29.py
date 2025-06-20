def tabelaPreco():
    x = 0
    print('Lojas Quase Dois - Tabela de preços')
    for i in range (51):
        if i != 0:
            x += 1.99
            print(f'{i} - R$ {x:.2f}')

inic = input('Tabela de preços (s/n): ')

if inic == 's' or inic == 'S':
    inic = tabelaPreco()