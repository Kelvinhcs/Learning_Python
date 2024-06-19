n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
tupla = (n1,n2,n3,n4)
pares = 0
print(f'O número 9 apareceu {tupla.count(9)} vez(es).' if tupla.count(9) >= 1 else 'O número 9 Não apareceu nenhuma vez.')
print(f'O número 3 apareceu na posição {tupla.index(3)+1}.' if 3 in tupla else 'O número 3 Não apareceu nenhuma vez.')
print(f'Os números pares digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        pares += 1
        print(f'{c} ', end='')
if pares == 0:
    print('NENHUM número par encontrado.')

