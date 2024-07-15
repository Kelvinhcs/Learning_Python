from moeda import numeros
digitado = float(input('Digite um o preço: R$'))
print(f'A metade de R${digitado:.2f} é R${numeros.metade(digitado):.2f}')
print(f'O dobro de R${digitado:.2f} é R${numeros.dobro(digitado):.2f}')
print(f'Aumentado 10% de {digitado:.2f}, temos R${numeros.aumentar(digitado, 10):.2f}')
print(f'Diminuindo 13% de {digitado:.2f}, temos R${numeros.diminuir(digitado, 13):.2f}')
