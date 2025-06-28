def prov():
    listGab = []
    nota = []
    insert = x = cont = z = 0
    aluno = 1
    medNot = 0
    y = True
    totalNota = []

    for a in range(10):
        z = input(f'Gabarito questão {a+1}:').upper()
        listGab.append(z)

    while y:
        for i in range(10):
            insert = input(f'Questão {i+1}: ').upper()
            nota.append(insert)

            if insert == listGab[i]:
                x += 1
                cont += 1
        totalNota.append(x)

        k = input('Novo aluno (1): ')
        if k == '1':
            aluno += 1
            x = 0

        else:
            y = False
            x = 0

    medNot = cont/aluno

    meNot = totalNota[0]
    mNot = totalNota[0]

    for y in range (len(totalNota)):
        if totalNota[y] > mNot:
            mNot = totalNota[y]
        if totalNota[y] < meNot:
            meNot = totalNota[y]

    print(f'Média das notas: {medNot:.2f}')
    print(f'Maior nota: {mNot}')
    print(f'Menor nota: {meNot}')

x = input('Iniciar verficação de notas (1): ')
if x == '1':
    x = prov()