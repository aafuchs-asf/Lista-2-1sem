def pedidoLanch():
    listCod = []
    listQnt = []
    cod = qnt = xi = xy = xk = xl = total =  0
    print(' Especificação Código Preço ')
    print('Cachorro Quente 100 R$ 1,20')
    print('Bauru Simples 101 R$ 1,30')
    print('Bauru com ovo 102 R$ 1,50')
    print('Hambúrguer 103 R$ 1,20')
    print('Cheeseburguer 104 R$ 1,30')
    print('Refrigerante 105 R$ 1,00')

    while True:
        cod = int(input('Código (digite 0 para encerrar): '))

        if cod == 0:
            break

        else:
            listCod.append(cod)
            qnt = int(input(f'Quantidade {cod}: '))
            listQnt.append(qnt)

    for i in range (len(listCod)):
        if listCod[i] == 100 or listCod[i] == 103:
            xy = listQnt[i] * 1.20
            print(f'Pedido: {listQnt[i]} de {listCod[i]}. Totalizando RS{xy:.2f}')
            total += xy

        if listCod[i] == 101 or listCod[i] == 104:
            xi = listQnt[i] * 1.30
            print(f'Pedido: {listQnt[i]} de {listCod[i]}. Totalizando RS{xi:.2f}')
            total += xi

        if listCod[i] == 102:
            xk = listQnt[i] * 1.50
            print(f'Pedido: {listQnt[i]} de {listCod[i]}. Totalizando RS{xk:.2f}')
            total += xk

        if listCod[i] == 105:
            xl = listQnt[i] * 1.00
            print(f'Pedido: {listQnt[i]} de {listCod[i]}. Totalizando RS{xl:.2f}')
            total += xl
         

        print(f'Total do pedido: RS{total:.2f}')

x = input('Iniciar pedido (1):')
if x =='1':
    x = pedidoLanch()