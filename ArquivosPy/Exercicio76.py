tup = ('Caderno', 15.00, 'Mochila', 120.00, 'Caneta', 3.00, 'Lápis', 1.50, 'Borracha', 2.00, 'Apontador', 2.50, 'Estojo', 20.00, 'Régua', 5.00, 'Tesoura', 6.00)
print('-'*35)
print(f'{"Listagem de preços":^35}')
print('-'*35)
for c in range(0, len(tup)):
    if c % 2 == 0:
        print(f'{tup[c]:.<20}',end='')
        print(f'R${tup[c+1]:>7.2f}')
print('-'*35)
