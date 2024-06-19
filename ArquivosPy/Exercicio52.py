numero = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, numero+1):
    if numero % c == 0:
        cont += 1
        print(f'\033[:33m{c}\033[:37:m', end=' ')
    else:
        print(c, end=' ')
print(f'\nO número {numero} foi dividido {cont} vezes')
if cont == 2:
    print('Este número É primo!!!')
else:
    print('Este número NÃO é primo.')


