def notaGinast(nome):
    print(f'Atleta: {nome}')
    nota = soma = medNota = 0
    listNota = []

    for i in range(5):
        nota = float(input('Nota: '))
        listNota.append(nota)


    mNota = listNota[0]
    meNota = listNota[0]

    for i in range (len(listNota)):
        if listNota[i] > mNota:
            mNota = listNota[i]
        if listNota[i] < meNota:
            meNota = listNota[i]

    listNota.remove(mNota)
    listNota.remove(meNota)

    for nota in listNota:
        soma += nota

    medNota = soma/ len(listNota)

    print(f'Melhor nota: {mNota}')
    print(f'Pior nota: {meNota}')
    print(f'Média dos demais saltos: {medNota:.2f}')
    print(f'Resultado final: ')
    print(f'{nome}: {medNota:.2f}')
    
x = input('Nome do Atleta: ')
y = notaGinast(x)