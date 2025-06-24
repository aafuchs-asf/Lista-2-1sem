def calcParc(valI):
    taxa = valF = valP = 0
    parc = 1
    print('Valor final  Juros  Parcela  Valor parcela')
    for i in range (5):
        valF = valI + (valI*(taxa/100))
        valP = valF/parc

        
        print(f'R${valF:.2f}   {taxa}    {parc}   R${valP:.2f}')

        parc += 2
        taxa += 5

a = int(input('Opções de parcelamento, digite 1: '))
val = 0.0
if a == 1:
    val = float(input('Valor da dívida: '))
    x = calcParc(val)