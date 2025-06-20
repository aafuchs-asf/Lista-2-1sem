# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada
# eleitor votar e ao final mostrar o número de votos de cada candidato.
def eleicao(eleitor):
    candid = []
    d = e = f = 0

    for i in range (eleitor):
        x = input('Digite a sigla do candidato (SSP/PPL/TDV): ')

        if x != 'SSP' and x != 'PPL' and x != 'TDV':
            print('Por favor, verifique se votou corretamente')
        else:
            candid.append(x)
            print('Voto concluido')
            print(candid)
   
    for i in candid:
        if i == 'SSP':
            d += 1
        elif i == 'PPL':
            e += 1
        elif i == 'TDV':
            f += 1
           
    print(candid)
    print(d,': votos para SSP')
    print(e,': votos para PPL')
    print(f,': votos para TDV')

eleitor = int(input('Digite a quantidade de eleitores: '))
a = eleicao(eleitor)