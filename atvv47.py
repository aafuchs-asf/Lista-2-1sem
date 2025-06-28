def notaGinast(nome):
    print(f'Atleta: {nome}')
    nota = soma = medNota = 0
    listNota = []

    for i in range(7):
        nota = float(input('Nota: '))
        listNota.append(nota)
        soma += nota

    medNota = soma/7

    mNota = listNota[0]
    meNota = listNota[0]

    for i in range (len(listNota)):
        if listNota[i] > mNota:
            mNota = listNota[i]
        if listNota[i] < meNota:
            meNota = listNota[i]
        

    print(f'Resultado final: ')
    print(f'Atleta: {nome}')
    print(f'Melhor nota: {mNota}')
    print(f'Pior nota: {meNota}')
    print(f'Média: {medNota:.2f}')
    
x = input('Nome do Atleta: ')
y = notaGinast(x)