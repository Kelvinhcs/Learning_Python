n = int(input('Digite um número para calcular o seu Fatorial: '))
f = 1
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
