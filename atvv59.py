tex = input('Digite o texto:').upper()
soma = 0

for vogal in tex:
    if vogal == 'A' or vogal == 'E' or vogal == 'I' or vogal == 'O' or vogal == 'U':
        soma += 1
print(f'O número de vogais no testo é: {soma}')