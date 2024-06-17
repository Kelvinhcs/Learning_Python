n = 1
pares = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impar += 1
print(f'Você digitou {pares} números pares e {impar} números impares')
