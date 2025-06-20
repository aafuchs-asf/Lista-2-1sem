name = input('Digite um nome: ')
idade = int(input('Digite sua idade: '))
sal = float(input('Digite o salário:'))
sexo = input('Digite o sexo (f/m)')
est = input('Digite o estado civil (s/c/v/d)')


while (idade<0 or idade>150):
    print('Idade invalida!')
    idade = int(input('Digite sua idade: '))

while (sal<=0):
    print('Salário invalido!')
    sal = float(input('Digite o salário:'))

while (sexo != 'f' and sexo != 'm'):
    print('Sexo invalido!')
    sexo = input('Digite o sexo (f/m)')

while (est != 's' and est != 'c' and est != 'v' and est != 'd' ):
    print('Estado cinvil invalido!')
    est = input('Digite o estado civil (s/c/v/d)')

for x in range (len(name)):
    while len(name)<3:
        print('Nome invalido!')
        name = input('Digite um nome: ')