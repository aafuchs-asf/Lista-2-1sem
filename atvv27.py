# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e
# a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
turma = int(input('Digite o número de turmas: '))
alunos = 0

for i in range(turma):
    y = True
    while y:
        b = int(input('Digite o número de alunos da turma: '))

        if b <= 40:
            alunos += b
            y = False

        else:
            print('As turmas não podem ter mais de 40 alunos.')
            alunos = 0

x = alunos/turma
print(x,' é a média de alunos por turma!')                                    