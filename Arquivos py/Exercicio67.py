while True:
    n = int(input('Digite um valor para mostrar a sua tabuada: '))
    print('-=-'*16)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:>2} = {n*c}')
    print('-=-'*16)
print('Programa encerrado.')
