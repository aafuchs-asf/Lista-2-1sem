# Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de
# idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
# conforme a média calculada.
def mediaIdade():
    y = True
    soma = ad = 0
    while y:
        x = float(input('Digite uma idade: '))
        ad += 1
        soma += x
        cond = input('Deseja adicionar outra idade(s/n)? ')
        if cond == 'n' or cond =='N':
            y = False
    result = soma/ad
    return result
 
a = mediaIdade()

if a >=0 and a <=25:
    print('Turma jovem')
if a >=26 and a <=60:
    print('Turma adulta')
if a > 60:
    print('Turma idosa')