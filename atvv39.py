listAlunos = []
cod = cm = 0

for i in range (4):
    cod = int(input('Código do aluno: '))
    cm = int(input('Altura aluno (cm): '))
    listAlunos.append([cod, cm])

meCm = listAlunos[0]
mCm = listAlunos[0]

for j in range(len(listAlunos)):
    if listAlunos[j][1] < meCm[1]:
        meCm = listAlunos[j]
    if listAlunos[j][1] > mCm[1]:
        mCm = listAlunos[j]
        
print(f'lista de códigos e alturas: {listAlunos}')
print(f'Menor altura (código, altura): {meCm}')
print(f'Maior altura (código, altura): {mCm}')