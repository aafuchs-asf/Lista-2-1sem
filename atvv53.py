listAlunos = []
cod = cm = soma = 0

while True:
    cod = int(input('Código do aluno (0 para encerrar): '))
    if cod == 0:
        break

    else:
        cm = int(input('Altura aluno (cm): '))
        listAlunos.append([cod, cm])

alt = int(input('Digite a altura (cm) que deseja consultar: '))
for cm in listAlunos:
    if cm[1] == alt:
        soma += 1
        
print(f'lista de códigos e alturas: {listAlunos}')
print(f'Número de alunos com {alt}cm: {soma}')