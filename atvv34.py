# Os números primos possuem várias aplicações dentro da Computação, por exemplo na criptografia. Um
# número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um
# número inteiro e determine se ele é ou não um número primo.
num = int(input('Digite um número: '))
y = True
w = v = 0

while y:
    for i in range(num):
        if i != 0 and i != 1 and v == 0:
            w = num%i

            if w == 0:
                print(num,'não é um número primo!')
                v = 1
                y = False

    if w != 0 and i != 1 and i != 0 and v == 0:
        print(num,'é um número primo!')
        y = False
        w = 0 