from moeda import numeros
digitado = float(input('Digite um o preço: R$'))
print(f'A metade de {numeros.moeda(digitado)} é {numeros.moeda(numeros.metade(digitado))}')
print(f'O dobro de {numeros.moeda(digitado)} é {numeros.moeda(numeros.dobro(digitado))}')
print(f'Aumentado 10% de {numeros.moeda(digitado)}, temos {numeros.moeda(numeros.aumentar(digitado, 10))}')
print(f'Diminuindo 13% de {numeros.moeda(digitado)}, temos {numeros.moeda(numeros.diminuir(digitado, 13))}')
