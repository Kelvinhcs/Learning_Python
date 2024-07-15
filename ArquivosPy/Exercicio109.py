from moeda import numeros
digitado = float(input('Digite um o preço: R$'))
print(f'A metade de {numeros.moeda(digitado)} é {numeros.metade(digitado, form=True)}')
print(f'O dobro de {numeros.moeda(digitado)} é {numeros.dobro(digitado, form=True)}')
print(f'Aumentado 10% de {numeros.moeda(digitado)}, temos {numeros.aumentar(digitado, 10, form=True)}')
print(f'Diminuindo 13% de {numeros.moeda(digitado)}, temos {numeros.diminuir(digitado, 13, form=True)}')
