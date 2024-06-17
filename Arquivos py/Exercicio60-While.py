n = int(input('Digite um número para calcular o seu fatorial: '))
f = 1
while n > 0:
    if n == 1:
        print(f'{n} = ', end='')
    else:
        print(f'{n} x ', end='')
    f *= n
    n -= 1
print(f)
