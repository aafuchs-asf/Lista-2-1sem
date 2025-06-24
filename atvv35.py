# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos
# existentes entre 1 e um número inteiro informado pelo usuário.
num = int(input('Digite um número: '))
y = True
w = v = p  = 0
j = []

for i in range(num+1):
    if i != 0:
        for x in range(i):
            if x != 0:
                w = 0
                w = i%x

                if w == 0:
                    j.append(x)

        if len(j) == 1:
            print(i,'é um número primo!')
            
    j.clear()