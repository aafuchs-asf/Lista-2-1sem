def eleicao():
    print('1 - Ciro Gomes')
    print('2 - Alexandre de Moraes')
    print('3 - Lula')
    print('4 - Roberto Dorner')
    print('5 - nulo')
    print('6 - Voto em Branco')
    vot = []
    inser = ciro = ale = lul = rob = br = nul = 0

    while True:
        inser = int(input('Voto (0 para encerrar): '))

        if inser == 0:
            break

        elif inser == 1 or inser == 2 or inser == 3 or inser == 4 or inser == 5 or inser == 6:
            vot.append(inser)

        else:
            print('Código inválido!')
        
    for i in vot:
        if i == 1:
            ciro += 1

        if i == 2:
            ale += 1

        if i == 3:
            lul += 1

        if i == 4:
            rob +=1

        if i == 5:
            nul += 1

        if i == 6:
            br += 1

    votNul = (nul/len(vot))*100
    votBr = (br/len(vot))*100

    print(f'{ciro} votos para Ciro Gomes')
    print(f'{ale} votos para Alexandre de Morais')
    print(f'{lul} votos para Lula')
    print(f'{rob} votos para Roberto Dorner')
    print(f'{votNul:.1f}% votos nulos')
    print(f'{votBr:.1f}% votos em branco')

    vot.clear

x = int(input('Iniciar votação (1): '))
if x == 1:
    x = eleicao()