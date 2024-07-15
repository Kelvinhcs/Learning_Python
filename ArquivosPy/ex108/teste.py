import moeda
digitado = float(input('Digite um o preço: R$'))
print(f'A metade de R${digitado:.2f} é R${moeda.metade(digitado):.2f}')
print(f'O dobro de R${digitado:.2f} é R${moeda.dobro(digitado):.2f}')
print(f'Aumentado 10% de {digitado:.2f}, temos R${moeda.aumentar(digitado, 10):.2f}')
print(f'Diminuindo 13% de {digitado:.2f}, temos R${moeda.diminuir(digitado, 13):.2f}')