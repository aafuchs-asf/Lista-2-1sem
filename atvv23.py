#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números
#primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
num = int(input('Digite um número: '))
y = True
w = v = p = soma = 0
j = []

for i in range(num+1):
    if i != 0:
        for x in range(i):
            if x != 0:
                w = 0
                w = i%x

                if w == 0:
                    j.append(x)

                else:
                     soma += 1

        if len(j) == 1:
            print(i,'é um número primo!')
            print(soma,' foi a quantidade de divisões para encontrar o número primo',i)

        else:
            print()
            print(j,' divisores do número', i)
            print()
    
    j.clear()


