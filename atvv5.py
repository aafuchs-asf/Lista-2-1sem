anos = 0
x = True
a = b = 0
taxa_a = taxa_b = 0.0

while x:
    if a <= b and taxa_a >= taxa_b:
        a = int(input('Insira o n° de habitantes da 1° população: '))
        taxa_a = float(input('Digite a taxa de crescimento da 1° população: '))
        b = int(input('Insira o n° de habitantes da 2° população: '))
        taxa_b = float(input('Insira a taxa de crescimento da 2° população: '))

        while a < b:
            anos += 1
            a += a*(taxa_a/100)
            b += b*(taxa_b/100)
            print(a,b)

        print(anos,'anos')

    y = input('Deseja repetir a operação? (s/n): ')
    if y == 'n':
        x = False
    else:
        a = b = taxa_a = taxa_b = 0